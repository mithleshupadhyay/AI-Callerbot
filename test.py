from twilio.rest import Client
import os

# Your Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = '+1XXXXXXXXXX'  # Replace with a verified phone number

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=to_number,
    from_=twilio_number,
    twiml="<Response><Say>Hello, this is a test call from Twilio!</Say></Response>"
)

print(f"Call SID: {call.sid}")
