from twilio.rest import Client
import random

otp_number = random.randint(1000, 9999)

# AUTHENTIFICATION OF TWILIO

phone_number = '+250786405263'

auth_sid = "ACe991a8e88df38d4f42d09211d69d4d70"
auth_token = "4e490f54b9c09376dddfd84755118b3e"

otp_client = Client(auth_sid, auth_token)

# Message that will OTP receiver get

otp_message = otp_client.messages.create(
    body="Your OTP number from oscar is "+str(otp_number),
    from_= "+12564880494",
    to= str(phone_number)
)
print('otp number is'+str(otp_number))

