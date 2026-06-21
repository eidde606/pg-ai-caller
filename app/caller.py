from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os


def make_call(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")
    to_number = os.getenv("TARGET_PHONE_NUMBER")

    client = Client(account_sid, auth_token)

    try:
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml=f"""
            <Response>
                <Say voice="alice">{message}</Say>
            </Response>
            """
        )

        return call.sid

    except TwilioRestException as e:
        print(f"Twilio Error: {e}")
        return None