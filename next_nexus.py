# https://github.com/mvexel/next_global_entry/blob/master/next_global_entry.py
"""Check for NEXUS interview openings in your city."""
import sys
import datetime
import time
import requests
from twilio.rest import Client
import twilio_config
from twilio_config import search_string

def main():
     # calculate date
    now = datetime.datetime.now()
    delta = datetime.timedelta(weeks=twilio_config.look_ahead_weeks)
    future = now + delta
    request_url = twilio_config.appt_query_url.format(
        timestamp=future.strftime("%Y-%m-%d"))
    result = requests.get(request_url).json()
    cities = [o.get('city').lower() for o in result]
    # print(cities)
    while True:
        if search_string.lower() in cities:
            client = Client(twilio_config.twilio_account, twilio_config.twilio_token)
            message = client.messages.create(
                to=twilio_config.to_number,
                from_=twilio_config.twilio_from_number,
                body=f"NEXUS interview opportunity in {search_string}\
                    opened up just now!")
            log("text message sent")
            sys.exit(0)
        else:
            log(f"No appointment found in {search_string} at the moment")
            time.sleep(1)

def log(text):
    """Write a one-line log message."""
    print("Log: {dt}\t//\t{msg}".format(
        dt=datetime.datetime.now(),
        msg=text))

if __name__ == '__main__':
   main()