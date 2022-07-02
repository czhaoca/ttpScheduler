# ttpScheduler


Orginial URL to get an appointment:
https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations?minimum=1&limit=10&serviceName=NEXUS

Note:
* This API shows locations with active appointment for service requested
* This API won't return available slot

Get location's appointment availability with input timeframe:
https://ttp.cbp.dhs.gov/schedulerapi/locations/13321/slots?startTimestamp=2022-07-05T00:00:00&endTimestamp=2022-10-02T00:00:00

Get all locations for TTP appointments:
https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations

Get all appointment available for Blaine Location
https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&locationId=13321&serviceName=NEXUS&limit=1000
Note:
* Limit to fetch 1000 slots
* change location id to modify which locaiton's slot to fetch
* returns empty list when no appointment is available
