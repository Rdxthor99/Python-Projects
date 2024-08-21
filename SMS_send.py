# Install the Twilio Python library first if you haven't already
# pip install twilio

from twilio.rest import Client

# Your Twilio account SID and auth token from https://www.twilio.com/console
account_sid = 'xxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxx'

# Your Twilio phone number (bought or verified) from https://www.twilio.com/console/phone-numbers/dashboard
twilio_phone_number = '+xxxxxxxxxx'

# The destination phone number you want to send the SMS to (in E.164 format)
destination_phone_number = input("Enter the destination phone number: ")

# Your message content
message_body = input("Enter the message you want to deliver: ")

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send the message
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=destination_phone_number
)

print(f'Message sent successfully. Message SID: {message.sid}')
