import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACb1ed9f3ef342270190ece78c46ca5db4'
auth_token = 'e4bc012a526570f13c4ec6530093d193'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18704510055',
                     to='+15734050170'
                 )

print(message.sid)
