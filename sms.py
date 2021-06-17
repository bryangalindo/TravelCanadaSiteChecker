from twilio.rest import Client
import constants as c


def send_sms_message(recipient_phone_number, twilio_phone_number, body):
    client = Client(c.TWILIO_ACCOUNT_SID, c.TWILIO_AUTH_TOKEN)
    return client.messages.create(
        to=recipient_phone_number, 
        from_=twilio_phone_number,
        body=body
        )
