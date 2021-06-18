import os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
PERSONAL_PHONE_NUMBER = os.getenv("PERSONAL_PHONE_NUMBER")

TRAVEL_CANADA_URL = "https://travel.gc.ca/travel-covid"
NOTIFICATION_TEXT = f"There was a change made on the Travel Canada website. Visit {TRAVEL_CANADA_URL}. Text STOP to opt out."
DATABASE = "travelcanada"
COLLECTION = "dates"

MONGO_DB_CONNECTION_STRING = os.getenv("MONGO_DB_CONNECTION_STRING")

EMPTY = 0
INITIAL_ID = 1
