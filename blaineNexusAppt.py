import sys
import time
import requests
import json
from datetime import datetime, timedelta

def main():
    # 13321 location id is Blaine location
    get_open_slot('5060')
    

def get_open_slot(loc_id='', appt_type='NEXUS'):
    # 
    count = 0
    while True:
        api_ret = fetch_api_details(loc_id, appt_type)
        if api_ret == []:
            count += 1
            print(f"No appointment available in Blaine for NEXUS.")
            print(f"API returns: {api_ret}")
            print(f"This is {count} time")
            print("************************************************")
            time.sleep(1)
        else:
            return api_ret

def fetch_api_details(loc_id='', appt_type='NEXUS'):
    appt_api_url = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&locationId="+loc_id+"&serviceName="+appt_type+"&limit=1000"

    return requests.get(appt_api_url).json()


    # appt_start = appt_details[0]["startTimestamp"]
    # print(f"Appointment Starts at: {appt_start}")
    
    # duration = appt_details[0]["duration"]
    # appt_end = appt_details[0]["endTimestamp"] 
    # print(f"Appointment duration: {duration} min")
    # print(f"Appointment Ends at: {appt_end}")

if __name__ == "__main__":
    main()