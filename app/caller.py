from twilio.rest import Client
import os

def make_call():
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")
    to_number = os.getenv("TARGET_PHONE_NUMBER")

    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=to_number,
        from_=from_number,
        twiml="""
        <Response>
            <Say>Hello. This is a test call.</Say>
        </Response>
        """
    )

    return call.sid