from bs4 import BeautifulSoup
import requests

import constants as c
import helpers as h


def get_travel_url_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")

def get_exemption_message(html):
    exemption_element = html.find("div", {"class": "alert alert-warning mrgn-tp-lg"})
    if exemption_element is not None:
        return h.convert_html_to_text(exemption_element)

def get_url_last_modified_date(html):
    last_modified_date_element = html.find("time")
    if last_modified_date_element is not None:
        return h.convert_html_to_text(last_modified_date_element)
