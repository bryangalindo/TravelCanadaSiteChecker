import os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
PERSONAL_PHONE_NUMBER = os.getenv("PERSONAL_PHONE_NUMBER")

TRAVEL_CANADA_URL = "https://travel.gc.ca/travel-covid"
EXEMPTION_TEXT = "Exemptions for fully vaccinated travellers who are eligible to enter Canada are expected in early July. Current travel restrictions still apply."

MONGO_DB_CONNECTION_STRING = os.getenv("MONGO_DB_CONNECTION_STRING")
