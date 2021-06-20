from datetime import datetime

import constants as c
from database import MongoDB
from scraper import get_travel_url_html, get_url_last_modified_date, get_exemption_message
from sms import send_sms_message


database = MongoDB(c.MONGO_DB_CONNECTION_STRING, c.MONGO_DB_DATABASE, c.MONGO_DB_COLLECTION)
html = get_travel_url_html(c.TRAVEL_CANADA_URL)

def check_if_collection_empty():
    if database.get_collection_size() == c.EMPTY:
        return True

def check_if_site_changed():
    last_inserted_date = database.get_last_document()['last_modified_date']
    scraped_date = get_url_last_modified_date(html)

    if scraped_date != last_inserted_date:
        return True

def insert_scraped_data():
    _dict = {
        "id": database.generate_id(),
        "timestamp": datetime.now(),
        "last_modified_date": get_url_last_modified_date(html),
        "message": get_exemption_message(html)
    }
    return database.insert_one_document(_dict)


if __name__ == '__main__':
    insert_scraped_data()
    is_changed = check_if_site_changed()
    if is_changed:
        send_sms_message(c.PERSONAL_PHONE_NUMBER, c.TWILIO_PHONE_NUMBER, c.NOTIFICATION_TEXT)
