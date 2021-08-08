#!/usr/bin/env python3

countries = {
   "United Arab Emirates": 
      {
         "currency_code": "AED"
      }
   ,
   "Afghanistan": 
      {
         "currency_code": "AFN"
      }
   ,
   "Albania": 
      {
         "currency_code": "ALL"
      }
   ,
   "Armenia": 
      {
         "currency_code": "AMD"
      }
   ,
   "Netherlands Antilles": 
      {
         "currency_code": "ANG"
      }
   ,
   "Angola": 
      {
         "currency_code": "AOA"
      }
   ,
   "Argentina": 
      {
         "currency_code": "ARS"
      }
   ,
   "Australia": 
      {
         "currency_code": "AUD"
      }
   ,
   "Aruba": 
      {
         "currency_code": "AWG"
      }
   ,
   "Azerbaijan": 
      {
         "currency_code": "AZN"
      }
   ,
   "Bosnia and Herzegovina": 
      {
         "currency_code": "BAM"
      }
   ,
   "Barbados": 
      {
         "currency_code": "BBD"
      }
   ,
   "Bangladesh": 
      {
         "currency_code": "BDT"
      }
   ,
   "Bulgaria": 
      {
         "currency_code": "BGN"
      }
   ,
   "Bahrain": 
      {
         "currency_code": "BHD"
      }
   ,
   "Burundi": 
      {
         "currency_code": "BIF"
      }
   ,
   "Bermuda": 
      {
         "currency_code": "BMD"
      }
   ,
   "Brunei": 
      {
         "currency_code": "BND"
      }
   ,
   "Bolivia": 
      {
         "currency_code": "BOB"
      }
   ,
   "Brazil": 
      {
         "currency_code": "BRL"
      }
   ,
   "Bahamas": 
      {
         "currency_code": "BSD"
      }
   ,
   "Bhutan": 
      {
         "currency_code": "BTN"
      }
   ,
   "Botswana": 
      {
         "currency_code": "BWP"
      }
   ,
   "Belarus": 
      {
         "currency_code": "BYN"
      }
   ,
   "Belize": 
      {
         "currency_code": "BZD"
      }
   ,
   "Canada": 
      {
         "currency_code": "CAD"
      }
   ,
   "Democratic Republic of the Congo": 
      {
         "currency_code": "CDF"
      }
   ,
   "Switzerland": 
      {
         "currency_code": "CHF"
      }
   ,
   "Chile": 
      {
         "currency_code": "CLP"
      }
   ,
   "China": 
      {
         "currency_code": "CNY"
      }
   ,
   "Colombia": 
      {
         "currency_code": "COP"
      }
   ,
   "Costa Rica": 
      {
         "currency_code": "CRC"
      }
   ,
   "Cuba": 
      {
         "currency_code": "CUC"
      },
   "Cape Verde": 
      {
         "currency_code": "CVE"
      }
   ,
   "Czech Republic": 
      {
         "currency_code": "CZK"
      }
   ,
   "Djibouti": 
      {
         "currency_code": "DJF"
      }
   ,
   "Denmark": 
      {
         "currency_code": "DKK"
      }
   ,
   "Dominican Republic": 
      {
         "currency_code": "DOP"
      }
   ,
   "Algeria": 
      {
         "currency_code": "DZD"
      }
   ,
   "Egypt": 
      {
         "currency_code": "EGP"
      }
   ,
   "Eritrea": 
      {
         "currency_code": "ERN"
      }
   ,
   "Ethiopia": 
      {
         "currency_code": "ETB"
      }
   ,
   "European Union": 
      {
         "currency_code": "EUR"
      }
   ,
   "Fiji": 
      {
         "currency_code": "FJD"
      }
   ,
   "Falkland Islands": 
      {
         "currency_code": "FKP"
      }
   ,
   "Faroe Islands": 
      {
         "currency_code": "FOK"
      }
   ,
   "United Kingdom": 
      {
         "currency_code": "GBP"
      }
   ,
   "Georgia": 
      {
         "currency_code": "GEL"
      }
   ,
   "Guernsey": 
      {
         "currency_code": "GGP"
      }
   ,
   "Ghana": 
      {
         "currency_code": "GHS"
      }
   ,
   "Gibraltar": 
      {
         "currency_code": "GIP"
      }
   ,
   "The Gambia": 
      {
         "currency_code": "GMD"
      }
   ,
   "Guinea": 
      {
         "currency_code": "GNF"
      }
   ,
   "Guatemala": 
      {
         "currency_code": "GTQ"
      }
   ,
   "Guyana": 
      {
         "currency_code": "GYD"
      }
   ,
   "Hong Kong": 
      {
         "currency_code": "HKD"
      }
   ,
   "Honduras": 
      {
         "currency_code": "HNL"
      }
   ,
   "Croatia": 
      {
         "currency_code": "HRK"
      }
   ,
   "Haiti": 
      {
         "currency_code": "HTG"
      }
   ,
   "Hungary": 
      {
         "currency_code": "HUF"
      }
   ,
   "Indonesia": 
      {
         "currency_code": "IDR"
      }
   ,
   "Israel": 
      {
         "currency_code": "ILS"
      }
   ,
   "Isle of Man": 
      {
         "currency_code": "IMP"
      }
   ,
   "India": 
      {
         "currency_code": "INR"
      }
   ,
   "Iraq": 
      {
         "currency_code": "IQD"
      }
   ,
   "Iran": 
      {
         "currency_code": "IRR"
      }
   ,
   "Iceland": 
      {
         "currency_code": "ISK"
      }
   ,
   "Jamaica": 
      {
         "currency_code": "JMD"
      }
   ,
   "Jordan": 
      {
         "currency_code": "JOD"
      }
   ,
   "Japan": 
      {
         "currency_code": "JPY"
      }
   ,
   "Kenya": 
      {
         "currency_code": "KES"
      }
   ,
   "Kyrgyzstan": 
      {
         "currency_code": "KGS"
      }
   ,
   "Cambodia": 
      {
         "currency_code": "KHR"
      }
   ,
   "Kiribati": 
      {
         "currency_code": "KID"
      }
   ,
   "Comoros": 
      {
         "currency_code": "KMF"
      }
   ,
   "South Korea": 
      {
         "currency_code": "KRW"
      }
   ,
   "Kuwait": 
      {
         "currency_code": "KWD"
      }
   ,
   "Cayman Islands": 
      {
         "currency_code": "KYD"
      }
   ,
   "Kazakhstan": 
      {
         "currency_code": "KZT"
      }
   ,
   "Laos": 
      {
         "currency_code": "LAK"
      }
   ,
   "Lebanon": 
      {
         "currency_code": "LBP"
      }
   ,
   "Sri Lanka": 
      {
         "currency_code": "LKR"
      }
   ,
   "Liberia": 
      {
         "currency_code": "LRD"
      }
   ,
   "Lesotho": 
      {
         "currency_code": "LSL"
      }
   ,
   "Libya": 
      {
         "currency_code": "LYD"
      }
   ,
   "Morocco": 
      {
         "currency_code": "MAD"
      }
   ,
   "Moldova": 
      {
         "currency_code": "MDL"
      }
   ,
   "Madagascar": 
      {
         "currency_code": "MGA"
      }
   ,
   "North Macedonia": 
      {
         "currency_code": "MKD"
      }
   ,
   "Myanmar": 
      {
         "currency_code": "MMK"
      }
   ,
   "Mongolia": 
      {
         "currency_code": "MNT"
      }
   ,
   "Macau": 
      {
         "currency_code": "MOP"
      }
   ,
   "Mauritania": 
      {
         "currency_code": "MRU"
      }
   ,
   "Mauritius": 
      {
         "currency_code": "MUR"
      }
   ,
   "Maldives": 
      {
         "currency_code": "MVR"
      }
   ,
   "Malawi": 
      {
         "currency_code": "MWK"
      }
   ,
   "Mexico": 
      {
         "currency_code": "MXN"
      }
   ,
   "Malaysia": 
      {
         "currency_code": "MYR"
      }
   ,
   "Mozambique": 
      {
         "currency_code": "MZN"
      }
   ,
   "Namibia": 
      {
         "currency_code": "NAD"
      }
   ,
   "Nigeria": 
      {
         "currency_code": "NGN"
      }
   ,
   "Nicaragua": 
      {
         "currency_code": "NIO"
      }
   ,
   "Norway": 
      {
         "currency_code": "NOK"
      }
   ,
   "Nepal": 
      {
         "currency_code": "NPR"
      }
   ,
   "New Zealand": 
      {
         "currency_code": "NZD"
      }
   ,
   "Oman": 
      {
         "currency_code": "OMR"
      }
   ,
   "Panama": 
      {
         "currency_code": "PAB"
      }
   ,
   "Peru": 
      {
         "currency_code": "PEN"
      }
   ,
   "Papua New Guinea": 
      {
         "currency_code": "PGK"
      }
   ,
   "Philippines": 
      {
         "currency_code": "PHP"
      }
   ,
   "Pakistan": 
      {
         "currency_code": "PKR"
      }
   ,
   "Poland": 
      {
         "currency_code": "PLN"
      }
   ,
   "Paraguay": 
      {
         "currency_code": "PYG"
      }
   ,
   "Qatar": 
      {
         "currency_code": "QAR"
      }
   ,
   "Romania": 
      {
         "currency_code": "RON"
      }
   ,
   "Serbia": 
      {
         "currency_code": "RSD"
      }
   ,
   "Russia": 
      {
         "currency_code": "RUB"
      }
   ,
   "Rwanda": 
      {
         "currency_code": "RWF"
      }
   ,
   "Saudi Arabia": 
      {
         "currency_code": "SAR"
      }
   ,
   "Solomon Islands": 
      {
         "currency_code": "SBD"
      }
   ,
   "Seychelles": 
      {
         "currency_code": "SCR"
      }
   ,
   "Sudan": 
      {
         "currency_code": "SDG"
      }
   ,
   "Sweden": 
      {
         "currency_code": "SEK"
      }
   ,
   "Singapore": 
      {
         "currency_code": "SGD"
      }
   ,
   "Saint Helena": 
      {
         "currency_code": "SHP"
      }
   ,
   "Sierra Leone": 
      {
         "currency_code": "SLL"
      }
   ,
   "Somalia": 
      {
         "currency_code": "SOS"
      }
   ,
   "Suriname": 
      {
         "currency_code": "SRD"
      }
   ,
   "South Sudan": 
      {
         "currency_code": "SSP"
      }
   ,
   "S�o Tom� and Pr�ncipe": 
      {
         "currency_code": "STN"
      }
   ,
   "Syria": 
      {
         "currency_code": "SYP"
      }
   ,
   "Eswatini": 
      {
         "currency_code": "SZL"
      }
   ,
   "Thailand": 
      {
         "currency_code": "THB"
      }
   ,
   "Tajikistan": 
      {
         "currency_code": "TJS"
      }
   ,
   "Turkmenistan": 
      {
         "currency_code": "TMT"
      }
   ,
   "Tunisia": 
      {
         "currency_code": "TND"
      }
   ,
   "Tonga": 
      {
         "currency_code": "TOP"
      }
   ,
   "Turkey": 
      {
         "currency_code": "TRY"
      }
   ,
   "Trinidad and Tobago": 
      {
         "currency_code": "TTD"
      }
   ,
   "Tuvalu": 
      {
         "currency_code": "TVD"
      }
   ,
   "Taiwan": 
      {
         "currency_code": "TWD"
      }
   ,
   "Tanzania": 
      {
         "currency_code": "TZS"
      }
   ,
   "Ukraine": 
      {
         "currency_code": "UAH"
      }
   ,
   "Uganda": 
      {
         "currency_code": "UGX"
      }
   ,
   "United States": 
      {
         "currency_code": "USD"
      }
   ,
   "Uruguay": 
      {
         "currency_code": "UYU"
      }
   ,
   "Uzbekistan": 
      {
         "currency_code": "UZS"
      }
   ,
   "Venezuela": 
      {
         "currency_code": "VES"
      }
   ,
   "Vietnam": 
      {
         "currency_code": "VND"
      }
   ,
   "Vanuatu": 
      {
         "currency_code": "VUV"
      }
   ,
   "Samoa": 
      {
         "currency_code": "WST"
      }
   ,
   "CEMAC": 
      {
         "currency_code": "XAF"
      }
   ,
   "Organisation of Eastern Caribbean States": 
      {
         "currency_code": "XCD"
      }
   ,
   "International Monetary Fund": 
      {
         "currency_code": "XDR"
      }
   ,
   "CFA": 
      {
         "currency_code": "XOF"
      }
   ,
   "Collectivit�s d'Outre-Mer": 
      {
         "currency_code": "XPF"
      }
   ,
   "Yemen": 
      {
         "currency_code": "YER"
      }
   ,
   "South Africa": 
      {
         "currency_code": "ZAR"
      }
   ,
   "Zambia": 
      {
         "currency_code": "ZMW"
      }
   
}