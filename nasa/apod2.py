#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("./nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds


def getDateInput():
    dateChoice = input("Enter a single date in YYYY-MM-DD Format :\n>> ").lower().strip()
    return dateChoice


# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    date_input = "date=" + getDateInput()

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds + "&" + date_input)

    ## strip off json
    apod = apodresp.json()

    #checking if media-type is an image and downloading and saving locally
    if apod.get("media_type") == "image":
        image_url = apod.get("url")

        response = requests.get(image_url)
        with open("apod.png", 'wb') as f:
            f.write(response.content)
    else:
        print("It returned media type other than image.")


if __name__ == "__main__":
    main()
