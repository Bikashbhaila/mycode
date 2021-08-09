#!/usr/bin/python3
import requests
import datetime

API_URL = "http://api.open-notify.org/iss-now.json"


def main():
    response = requests.get(API_URL)
    # convert response to json
    jsonResponse = response.json()

    print(jsonResponse)
    iss_position = jsonResponse.get("iss_position")
    timestamp = jsonResponse.get("timestamp")
    human_time = datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)
    
    print("CURRENT LOCATION OF THE ISS:")
    print("Timestamp:", human_time)
    print("Lon:", iss_position["longitude"])
    print("Lat:", iss_position["latitude"])




if __name__ == "__main__":
    main()
  