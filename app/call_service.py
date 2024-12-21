from twilio.rest import Client
import os

def make_call(phone_number, message):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_number = os.getenv('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)
    call = client.calls.create(
        twiml=f'<Response><Say>{message}</Say></Response>',
        to=phone_number,
        from_=from_number
    )
    return call.sid
