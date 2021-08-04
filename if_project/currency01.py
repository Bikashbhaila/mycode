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
            }
         }

country_input = ""
amount_input = 0

while country_input not in countries:
    country_input = input("Please select a country from below list:\n[Nepal, Vietnam, Singapore]\n=> ").title().strip()
    
    if country_input in countries:
        amount_input = int(input("Enter your net worth in US Dollars:\n=> "))
        converted_amount = amount_input * countries[country_input]["xchange_rate"]
        if converted_amount >= 1000000000:
            print("Congrat$, You are a BILLIONNAIRE in", country_input, "and your net-worth is", countries[country_input]["currency_code"], converted_amount)
        elif converted_amount >= 1000000:           
            print("Congrat$, You are a MILLIONNAIRE in", country_input, "and your net-worth is", countries[country_input]["currency_code"], converted_amount)
        else:
            print("Sorry, You are poor!!!")
