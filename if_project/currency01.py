#!/usr/bin/env python3

countries = {
            "Nepal": { 
                    "currency_code": "NPR",
                    "xchange_rate": 118.74 
                    },
            "Vietnam": {
                    "currency_code": "VND",
                    "xchange_rate": 22955 
                    },
            "Singapore": {
                    "currency_code": "SGD",
                    "xchange_rate": 1.35 
                    },
            "Korea": {
                    "currency_code": "KRW",
                    "xchange_rate": 1145.85
                    },
            "England": {
                    "currency_code": "GBP",
                    "xchange_rate": 0.72
                    }
             }  

country_input = ""
amount_input = 0

while country_input not in countries:

    country_input = input(f"Please select a country from below list:\n{list(countries.keys())}\n=> ").title().strip()
    
    if country_input in countries:
        try:
            amount_input = int(input("Enter your net worth in US Dollars:\n=> "))
            converted_amount = amount_input * countries[country_input]["xchange_rate"]
            if converted_amount >= 1000000000:
                print("Congrat$, You are a BILLIONNAIRE in", country_input, "and your net-worth is", countries[country_input]["currency_code"], converted_amount)
            elif converted_amount >= 1000000:
                print("Congrat$, You are a MILLIONNAIRE in", country_input, "and your net-worth is", countries[country_input]["currency_code"], converted_amount)
            else:
                print(f"Sorry, You are not millionaire in {country_input} yet...")    
        except ValueError as response:
            print(response)
            print("Non-numerical value entered")
