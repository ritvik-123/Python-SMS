from twilio.rest import Client

account_sid = 'ACc18d4dd94489124e77937d71cd796629'
auth_token = '2484f2978334820132b2c4438c1f279e'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGdde1ba008827693d0635a9048b93cdb7',
    body='hello',
    to='+919958281499'
)

print(message.sid)
