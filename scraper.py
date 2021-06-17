import logging

from bs4 import BeautifulSoup
import requests

import constants as c
import helpers as h


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def get_travel_url_html():
    logger.info('Scraping starting')
    response = requests.get(c.TRAVEL_CANADA_URL)
    logger.info('Scraping complete')
    if response.status_code == 200:
        logger.info('Scrape successful')
        return BeautifulSoup(response.content, "html.parser")

def get_exemption_message(html):
    exemption_element = html.find("div", {"class": "alert alert-warning mrgn-tp-lg"})
    if exemption_element is not None:
        return h.convert_html_to_text(exemption_element)

def get_url_last_modified_date(html):
    last_modified_date_element = html.find("time")
    if last_modified_date_element is not None:
        return h.convert_html_to_text(last_modified_date_element)
