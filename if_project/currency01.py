#!/usr/bin/env python3
import requests
from countries_list import countries

BASE_API_URL = "https://v6.exchangerate-api.com/v6/"    # base api url to fetch exchange rate

def startGame():
    country_input = ""
    amount_input = 0

    while country_input not in countries:
        country_input = input(f"Please select any country in the globe:\n=> ").title().strip()
        
        if country_input in countries:
            # get country_input's currency code from countries_list dictionary
            currency_code = countries[country_input]["currency_code"].strip().upper()
            # prompt user to enter amount and pass currency code and amount_input to getExchangeRate for API Call
            try:
                amount_input = int(input("Enter your net worth in US Dollars:\n=> USD "))
                getExchangeRate(country_input, amount_input, currency_code)
            except ValueError as response:
                print(response)
                print("Non-numerical value entered. Net worth must be a number")
                amount_input = int(input("Enter your net worth in US Dollars:\n=> USD "))
                getExchangeRate(country_input, amount_input, currency_code)
        else: 
            # prompt user to enter again if country_input not in countries dictionary
            print(f"Invalid country: {country_input}. Please enter a valid country name.\n=> ")


def getExchangeRate(country_input, amount_input, currency_code):
    # read api-key from cred file
    with open("currency.cred") as mycred:
        cred = mycred.read().strip("\n")
    
    API_URL = (f"{BASE_API_URL}{cred}/pair/USD/{currency_code}")

    # send GET request and get exchange rate
    response = requests.get(API_URL)
    exchange_rate = response.json().get('conversion_rate')
   # pass exchange rate and to showNetWorth(exchange_rate, amount_input)
    displayNetWorth(exchange_rate, country_input, currency_code,amount_input)


def displayNetWorth(exchange_rate, country_input, currency_code, amount_input):
    # calculate netWorth and display if millionaire or billionaire
    userNetWorth = exchange_rate * amount_input
    userNetWorth_formatted = "{:,.2f}".format(userNetWorth)
    if userNetWorth >= 1000000000:
        print("Congrat$, You are a BILLIONNAIRE in", country_input, "and your net-worth is", currency_code, userNetWorth_formatted)
    elif userNetWorth >= 1000000:
        print("Congrat$, You are a MILLIONNAIRE in", country_input, "and your net-worth is", currency_code, userNetWorth_formatted)
    else:
        print(f"Sorry, You are not millionaire in {country_input} yet... You net-worth is just", currency_code, userNetWorth_formatted)


def main():
    print("Welcome to <<ARE YOU A MILLIONAIRE SOMEWHERE IN THE WORLD IN REALTIME?>>")
    
    while True:
        startGame() 
        playAgain = input("Do you want to try another country? Please type yes or no.\n=> ").lower()
        if playAgain == "yes":
            continue
        elif playAgain == "no" or playAgain != "yes":
            print("GoodBye!!!")
            break

if __name__ == "__main__":
    main()
