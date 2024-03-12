# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "ACa474285d73ed27e091257ac025236026"
auth_token = "3e23bdaea75c4a1bd60e19ee1123168d"
client = Client(account_sid, auth_token)


def call(audio_url, to_number="+919494517819"):
    call = client.calls.create(
        url=audio_url,
        to=to_number,
        from_="+17074193696")
    print(call.sid)

# call(to_number="+916281462828")
