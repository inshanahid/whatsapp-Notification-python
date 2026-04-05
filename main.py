from twilio.rest import Client
from datetime import datetime, timedelta
import time 
import os
from dotenv import load_dotenv

# load env file
load_dotenv()

# step 2 --> twilio credentials
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

# step --> 3 function to send whatsapp message
def send_whatsapp_message(recipient_number, message_body):  # fixed spelling
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'   # fixed variable
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')   # improved error message

# step-4 user input
name = input('enter the recipient name= ')
recipient_number = input('enter the recipient whatsapp number with country code (e.g, +12345)= ')
message_body = input(f'enter the message you want to send to {name}: ')

# step-5 parse date/time and calculate delay
date_str = input('enter the date to send the message(YYYY-MM-DD): ')
time_str = input('enter the time to send the message(HH:MM in 24hours format): ')

# datetime
try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
except ValueError:
    print('Invalid date/time format')
    exit()

current_datetime = datetime.now()

# calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('the specified time is in the past. please enter a future date and time')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
    
    # wait until the scheduled time
    time.sleep(delay_seconds)

    # send the message
    send_whatsapp_message(recipient_number, message_body)