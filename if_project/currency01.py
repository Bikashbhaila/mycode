#!/usr/bin/env python3
import requests
from countries_list import countries

API_URL = "https://v6.exchangerate-api.com/v6/6cd5694c638bd04a1912f18d/latest/USD"

def startGame():
    print("Welcome to <<ARE YOU A MILLIONAIRE SOMEWHERE IN THE WORLD IN REALTIME?>>")
    
    country_input = ""
    amount_input = 0

    while country_input not in list(countries["country"]):
        country_input = input(f"Please select any country in the globe:\n=> ").title().strip()
    
        if country_input in countries:
            try:
                amount_input = int(input("Enter your net worth in US Dollars:\n=>USD "))
                getExchangeRate(country_input, amount_input)
            except ValueError as response:
                print(response)
                print("Non-numerical value entered")

def getExchangeRate(country_input, amount_input):
    print(country_input, amount_input)

def calculateNetWorth():
    converted_amount = amount_input * countries[country_input]["xchange_rate"]
    if converted_amount >= 1000000000:
        print("Congrat$, You are a BILLIONNAIRE in", country_input, "and your net-worth is", countries[country_input]["currency_code"], converted_amount)
    elif converted_amount >= 1000000:
        print("Congrat$, You are a MILLIONNAIRE in", country_input, "and your net-worth is", countries[country_input]["currency_code"], converted_amount)
    else:
        print(f"Sorry, You are not millionaire in {country_input} yet...")


def main() :
    while True:
        startGame()
        getExchangeRate(country_input, amount_input)
        #calculateNetWorth()
        
        playAgain = input("Do you want to try another country?")
        if playAgain == "yes":
            continue
        else:
            print("GoodBye!!!")
            break

if __name__ == "__main__":
    main()
