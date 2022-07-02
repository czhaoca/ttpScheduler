import sys
import requests
import json
from datetime import datetime, timedelta

def main():
    # while True:
    #     try:
    #         if len(sys.argv) < 2:
    #             sys.exit("Missing command-line argument")
    #         elif len(sys.argv) > 2:
    #             sys.exit("Extra command-line argument")
    #         else:
    #             amount = float(sys.argv[1])
    #             break
    #     except ValueError:
    #         sys.exit("Command-line argument is not a number")
    loc_id = str(13321)
    get_open_slot(loc_id)

def get_all_loc():
    LOCATIONS_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations?limit=300"

    print("Retrieving locations...")
    locations = requests.get(LOCATIONS_URL).json()

    for loc in locations:
        print("{}, {}: {} ({})".format(
    loc['city'], loc['state'], loc['name'].strip(), loc['id']
        ))

def get_open_slot(loc_id):
    TIMESPAN_URL = "https://ttp.cbp.dhs.gov/schedulerapi/locations/13321/slots?startTimestamp={}&endTimestamp={}"

    start_time = datetime.now()
    start_time.replace(microsecond=0)
    results = True
    i = 1

    while results:
        end_time = start_time + timedelta(days=30)
        url = TIMESPAN_URL.format(start_time.isoformat(), end_time.isoformat())
        slots = requests.get(url).json()
        available_slots = [slot['timestamp'] for slot in slots if slot['active'] == 1]
        print("{} - {}: {} slots available".format(start_time, end_time, len(available_slots)))
        if available_slots or i == 12:
            break
        start_time = end_time
        i += 1

def appt_time(location):
    location = str(location)
    appt_api_url = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId=" + location +"&minimum=1"
    appt_details = requests.get(appt_api_url).json()

    # print(appt_api_url)

    appt_start = appt_details[0]["startTimestamp"]
    print(f"Appointment Starts at: {appt_start}")
    
    duration = appt_details[0]["duration"]
    appt_end = appt_details[0]["endTimestamp"] 
    print(f"Appointment duration: {duration} min")
    print(f"Appointment Ends at: {appt_end}")

if __name__ == "__main__":
    main()