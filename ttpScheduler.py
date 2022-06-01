import sys
import requests
import json

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

    response = requests.get("https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations?minimum=1&limit=&serviceName=NEXUS")
    o = response.json()
    id = o[0]["id"]
    short_name = o[0]["shortName"]
    print(f"id: {id}")
    print(f"Appiontment Centre: {short_name}\n")

    appt_time(id)

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

    # print(json.dumps(appt_details, indent=2))

if __name__ == "__main__":
    main()