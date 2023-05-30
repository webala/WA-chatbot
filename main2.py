from twilio.rest import Client

account_sid = 'AC5cdc7eb4238b590b1b7812249dc41f78'
auth_token = '206fa39128070cd8c216ce04532b4a4d'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to='+254791055897',
    from_='+13158126252',
    body='Hi there. This is Mr. Robot chatbot.'
)

print(message.sid)