#!/usr/bin/env python3

countries = {
  {
    "currency_code": "AED",
    "currency_name": "UAE Dirham",
    "country": "United Arab Emirates"
  },
  {
    "currency_code": "AFN",
    "currency_name": "Afghan Afghani",
    "country": "Afghanistan"
  },
  {
    "currency_code": "ALL",
    "currency_name": "Albanian Lek",
    "country": "Albania"
  },
  {
    "currency_code": "AMD",
    "currency_name": "Armenian Dram",
    "country": "Armenia"
  },
  {
    "currency_code": "ANG",
    "currency_name": "Netherlands Antillian Guilder",
    "country": "Netherlands Antilles"
  },
  {
    "currency_code": "AOA",
    "currency_name": "Angolan Kwanza",
    "country": "Angola"
  },
  {
    "currency_code": "ARS",
    "currency_name": "Argentine Peso",
    "country": "Argentina"
  },
  {
    "currency_code": "AUD",
    "currency_name": "Australian Dollar",
    "country": "Australia"
  },
  {
    "currency_code": "AWG",
    "currency_name": "Aruban Florin",
    "country": "Aruba"
  },
  {
    "currency_code": "AZN",
    "currency_name": "Azerbaijani Manat",
    "country": "Azerbaijan"
  },
  {
    "currency_code": "BAM",
    "currency_name": "Bosnia and Herzegovina Mark",
    "country": "Bosnia and Herzegovina"
  },
  {
    "currency_code": "BBD",
    "currency_name": "Barbados Dollar",
    "country": "Barbados"
  },
  {
    "currency_code": "BDT",
    "currency_name": "Bangladeshi Taka",
    "country": "Bangladesh"
  },
  {
    "currency_code": "BGN",
    "currency_name": "Bulgarian Lev",
    "country": "Bulgaria"
  },
  {
    "currency_code": "BHD",
    "currency_name": "Bahraini Dinar",
    "country": "Bahrain"
  },
  {
    "currency_code": "BIF",
    "currency_name": "Burundian Franc",
    "country": "Burundi"
  },
  {
    "currency_code": "BMD",
    "currency_name": "Bermudian Dollar",
    "country": "Bermuda"
  },
  {
    "currency_code": "BND",
    "currency_name": "Brunei Dollar",
    "country": "Brunei"
  },
  {
    "currency_code": "BOB",
    "currency_name": "Bolivian Boliviano",
    "country": "Bolivia"
  },
  {
    "currency_code": "BRL",
    "currency_name": "Brazilian Real",
    "country": "Brazil"
  },
  {
    "currency_code": "BSD",
    "currency_name": "Bahamian Dollar",
    "country": "Bahamas"
  },
  {
    "currency_code": "BTN",
    "currency_name": "Bhutanese Ngultrum",
    "country": "Bhutan"
  },
  {
    "currency_code": "BWP",
    "currency_name": "Botswana Pula",
    "country": "Botswana"
  },
  {
    "currency_code": "BYN",
    "currency_name": "Belarusian Ruble",
    "country": "Belarus"
  },
  {
    "currency_code": "BZD",
    "currency_name": "Belize Dollar",
    "country": "Belize"
  },
  {
    "currency_code": "CAD",
    "currency_name": "Canadian Dollar",
    "country": "Canada"
  },
  {
    "currency_code": "CDF",
    "currency_name": "Congolese Franc",
    "country": "Democratic Republic of the Congo"
  },
  {
    "currency_code": "CHF",
    "currency_name": "Swiss Franc",
    "country": "Switzerland"
  },
  {
    "currency_code": "CLP",
    "currency_name": "Chilean Peso",
    "country": "Chile"
  },
  {
    "currency_code": "CNY",
    "currency_name": "Chinese Renminbi",
    "country": "China"
  },
  {
    "currency_code": "COP",
    "currency_name": "Colombian Peso",
    "country": "Colombia"
  },
  {
    "currency_code": "CRC",
    "currency_name": "Costa Rican Colon",
    "country": "Costa Rica"
  },
  {
    "currency_code": "CUC",
    "currency_name": "Cuban Convertible Peso",
    "country": "Cuba"
  },
  {
    "currency_code": "CUP",
    "currency_name": "Cuban Peso",
    "country": "Cuba"
  },
  {
    "currency_code": "CVE",
    "currency_name": "Cape Verdean Escudo",
    "country": "Cape Verde"
  },
  {
    "currency_code": "CZK",
    "currency_name": "Czech Koruna",
    "country": "Czech Republic"
  },
  {
    "currency_code": "DJF",
    "currency_name": "Djiboutian Franc",
    "country": "Djibouti"
  },
  {
    "currency_code": "DKK",
    "currency_name": "Danish Krone",
    "country": "Denmark"
  },
  {
    "currency_code": "DOP",
    "currency_name": "Dominican Peso",
    "country": "Dominican Republic"
  },
  {
    "currency_code": "DZD",
    "currency_name": "Algerian Dinar",
    "country": "Algeria"
  },
  {
    "currency_code": "EGP",
    "currency_name": "Egyptian Pound",
    "country": "Egypt"
  },
  {
    "currency_code": "ERN",
    "currency_name": "Eritrean Nakfa",
    "country": "Eritrea"
  },
  {
    "currency_code": "ETB",
    "currency_name": "Ethiopian Birr",
    "country": "Ethiopia"
  },
  {
    "currency_code": "EUR",
    "currency_name": "Euro",
    "country": "European Union"
  },
  {
    "currency_code": "FJD",
    "currency_name": "Fiji Dollar",
    "country": "Fiji"
  },
  {
    "currency_code": "FKP",
    "currency_name": "Falkland Islands Pound",
    "country": "Falkland Islands"
  },
  {
    "currency_code": "FOK",
    "currency_name": "Faroese Kr�na",
    "country": "Faroe Islands"
  },
  {
    "currency_code": "GBP",
    "currency_name": "Pound Sterling",
    "country": "United Kingdom"
  },
  {
    "currency_code": "GEL",
    "currency_name": "Georgian Lari",
    "country": "Georgia"
  },
  {
    "currency_code": "GGP",
    "currency_name": "Guernsey Pound",
    "country": "Guernsey"
  },
  {
    "currency_code": "GHS",
    "currency_name": "Ghanaian Cedi",
    "country": "Ghana"
  },
  {
    "currency_code": "GIP",
    "currency_name": "Gibraltar Pound",
    "country": "Gibraltar"
  },
  {
    "currency_code": "GMD",
    "currency_name": "Gambian Dalasi",
    "country": "The Gambia"
  },
  {
    "currency_code": "GNF",
    "currency_name": "Guinean Franc",
    "country": "Guinea"
  },
  {
    "currency_code": "GTQ",
    "currency_name": "Guatemalan Quetzal",
    "country": "Guatemala"
  },
  {
    "currency_code": "GYD",
    "currency_name": "Guyanese Dollar",
    "country": "Guyana"
  },
  {
    "currency_code": "HKD",
    "currency_name": "Hong Kong Dollar",
    "country": "Hong Kong"
  },
  {
    "currency_code": "HNL",
    "currency_name": "Honduran Lempira",
    "country": "Honduras"
  },
  {
    "currency_code": "HRK",
    "currency_name": "Croatian Kuna",
    "country": "Croatia"
  },
  {
    "currency_code": "HTG",
    "currency_name": "Haitian Gourde",
    "country": "Haiti"
  },
  {
    "currency_code": "HUF",
    "currency_name": "Hungarian Forint",
    "country": "Hungary"
  },
  {
    "currency_code": "IDR",
    "currency_name": "Indonesian Rupiah",
    "country": "Indonesia"
  },
  {
    "currency_code": "ILS",
    "currency_name": "Israeli New Shekel",
    "country": "Israel"
  },
  {
    "currency_code": "IMP",
    "currency_name": "Manx Pound",
    "country": "Isle of Man"
  },
  {
    "currency_code": "INR",
    "currency_name": "Indian Rupee",
    "country": "India"
  },
  {
    "currency_code": "IQD",
    "currency_name": "Iraqi Dinar",
    "country": "Iraq"
  },
  {
    "currency_code": "IRR",
    "currency_name": "Iranian Rial",
    "country": "Iran"
  },
  {
    "currency_code": "ISK",
    "currency_name": "Icelandic Kr�na",
    "country": "Iceland"
  },
  {
    "currency_code": "JMD",
    "currency_name": "Jamaican Dollar",
    "country": "Jamaica"
  },
  {
    "currency_code": "JOD",
    "currency_name": "Jordanian Dinar",
    "country": "Jordan"
  },
  {
    "currency_code": "JPY",
    "currency_name": "Japanese Yen",
    "country": "Japan"
  },
  {
    "currency_code": "KES",
    "currency_name": "Kenyan Shilling",
    "country": "Kenya"
  },
  {
    "currency_code": "KGS",
    "currency_name": "Kyrgyzstani Som",
    "country": "Kyrgyzstan"
  },
  {
    "currency_code": "KHR",
    "currency_name": "Cambodian Riel",
    "country": "Cambodia"
  },
  {
    "currency_code": "KID",
    "currency_name": "Kiribati Dollar",
    "country": "Kiribati"
  },
  {
    "currency_code": "KMF",
    "currency_name": "Comorian Franc",
    "country": "Comoros"
  },
  {
    "currency_code": "KRW",
    "currency_name": "South Korean Won",
    "country": "South Korea"
  },
  {
    "currency_code": "KWD",
    "currency_name": "Kuwaiti Dinar",
    "country": "Kuwait"
  },
  {
    "currency_code": "KYD",
    "currency_name": "Cayman Islands Dollar",
    "country": "Cayman Islands"
  },
  {
    "currency_code": "KZT",
    "currency_name": "Kazakhstani Tenge",
    "country": "Kazakhstan"
  },
  {
    "currency_code": "LAK",
    "currency_name": "Lao Kip",
    "country": "Laos"
  },
  {
    "currency_code": "LBP",
    "currency_name": "Lebanese Pound",
    "country": "Lebanon"
  },
  {
    "currency_code": "LKR",
    "currency_name": "Sri Lanka Rupee",
    "country": "Sri Lanka"
  },
  {
    "currency_code": "LRD",
    "currency_name": "Liberian Dollar",
    "country": "Liberia"
  },
  {
    "currency_code": "LSL",
    "currency_name": "Lesotho Loti",
    "country": "Lesotho"
  },
  {
    "currency_code": "LYD",
    "currency_name": "Libyan Dinar",
    "country": "Libya"
  },
  {
    "currency_code": "MAD",
    "currency_name": "Moroccan Dirham",
    "country": "Morocco"
  },
  {
    "currency_code": "MDL",
    "currency_name": "Moldovan Leu",
    "country": "Moldova"
  },
  {
    "currency_code": "MGA",
    "currency_name": "Malagasy Ariary",
    "country": "Madagascar"
  },
  {
    "currency_code": "MKD",
    "currency_name": "Macedonian Denar",
    "country": "North Macedonia"
  },
  {
    "currency_code": "MMK",
    "currency_name": "Burmese Kyat",
    "country": "Myanmar"
  },
  {
    "currency_code": "MNT",
    "currency_name": "Mongolian T�gr�g",
    "country": "Mongolia"
  },
  {
    "currency_code": "MOP",
    "currency_name": "Macanese Pataca",
    "country": "Macau"
  },
  {
    "currency_code": "MRU",
    "currency_name": "Mauritanian Ouguiya",
    "country": "Mauritania"
  },
  {
    "currency_code": "MUR",
    "currency_name": "Mauritian Rupee",
    "country": "Mauritius"
  },
  {
    "currency_code": "MVR",
    "currency_name": "Maldivian Rufiyaa",
    "country": "Maldives"
  },
  {
    "currency_code": "MWK",
    "currency_name": "Malawian Kwacha",
    "country": "Malawi"
  },
  {
    "currency_code": "MXN",
    "currency_name": "Mexican Peso",
    "country": "Mexico"
  },
  {
    "currency_code": "MYR",
    "currency_name": "Malaysian Ringgit",
    "country": "Malaysia"
  },
  {
    "currency_code": "MZN",
    "currency_name": "Mozambican Metical",
    "country": "Mozambique"
  },
  {
    "currency_code": "NAD",
    "currency_name": "Namibian Dollar",
    "country": "Namibia"
  },
  {
    "currency_code": "NGN",
    "currency_name": "Nigerian Naira",
    "country": "Nigeria"
  },
  {
    "currency_code": "NIO",
    "currency_name": "Nicaraguan C�rdoba",
    "country": "Nicaragua"
  },
  {
    "currency_code": "NOK",
    "currency_name": "Norwegian Krone",
    "country": "Norway"
  },
  {
    "currency_code": "NPR",
    "currency_name": "Nepalese Rupee",
    "country": "Nepal"
  },
  {
    "currency_code": "NZD",
    "currency_name": "New Zealand Dollar",
    "country": "New Zealand"
  },
  {
    "currency_code": "OMR",
    "currency_name": "Omani Rial",
    "country": "Oman"
  },
  {
    "currency_code": "PAB",
    "currency_name": "Panamanian Balboa",
    "country": "Panama"
  },
  {
    "currency_code": "PEN",
    "currency_name": "Peruvian Sol",
    "country": "Peru"
  },
  {
    "currency_code": "PGK",
    "currency_name": "Papua New Guinean Kina",
    "country": "Papua New Guinea"
  },
  {
    "currency_code": "PHP",
    "currency_name": "Philippine Peso",
    "country": "Philippines"
  },
  {
    "currency_code": "PKR",
    "currency_name": "Pakistani Rupee",
    "country": "Pakistan"
  },
  {
    "currency_code": "PLN",
    "currency_name": "Polish Z?oty",
    "country": "Poland"
  },
  {
    "currency_code": "PYG",
    "currency_name": "Paraguayan Guaran�",
    "country": "Paraguay"
  },
  {
    "currency_code": "QAR",
    "currency_name": "Qatari Riyal",
    "country": "Qatar"
  },
  {
    "currency_code": "RON",
    "currency_name": "Romanian Leu",
    "country": "Romania"
  },
  {
    "currency_code": "RSD",
    "currency_name": "Serbian Dinar",
    "country": "Serbia"
  },
  {
    "currency_code": "RUB",
    "currency_name": "Russian Ruble",
    "country": "Russia"
  },
  {
    "currency_code": "RWF",
    "currency_name": "Rwandan Franc",
    "country": "Rwanda"
  },
  {
    "currency_code": "SAR",
    "currency_name": "Saudi Riyal",
    "country": "Saudi Arabia"
  },
  {
    "currency_code": "SBD",
    "currency_name": "Solomon Islands Dollar",
    "country": "Solomon Islands"
  },
  {
    "currency_code": "SCR",
    "currency_name": "Seychellois Rupee",
    "country": "Seychelles"
  },
  {
    "currency_code": "SDG",
    "currency_name": "Sudanese Pound",
    "country": "Sudan"
  },
  {
    "currency_code": "SEK",
    "currency_name": "Swedish Krona",
    "country": "Sweden"
  },
  {
    "currency_code": "SGD",
    "currency_name": "Singapore Dollar",
    "country": "Singapore"
  },
  {
    "currency_code": "SHP",
    "currency_name": "Saint Helena Pound",
    "country": "Saint Helena"
  },
  {
    "currency_code": "SLL",
    "currency_name": "Sierra Leonean Leone",
    "country": "Sierra Leone"
  },
  {
    "currency_code": "SOS",
    "currency_name": "Somali Shilling",
    "country": "Somalia"
  },
  {
    "currency_code": "SRD",
    "currency_name": "Surinamese Dollar",
    "country": "Suriname"
  },
  {
    "currency_code": "SSP",
    "currency_name": "South Sudanese Pound",
    "country": "South Sudan"
  },
  {
    "currency_code": "STN",
    "currency_name": "S�o Tom� and Pr�ncipe Dobra",
    "country": "S�o Tom� and Pr�ncipe"
  },
  {
    "currency_code": "SYP",
    "currency_name": "Syrian Pound",
    "country": "Syria"
  },
  {
    "currency_code": "SZL",
    "currency_name": "Eswatini Lilangeni",
    "country": "Eswatini"
  },
  {
    "currency_code": "THB",
    "currency_name": "Thai Baht",
    "country": "Thailand"
  },
  {
    "currency_code": "TJS",
    "currency_name": "Tajikistani Somoni",
    "country": "Tajikistan"
  },
  {
    "currency_code": "TMT",
    "currency_name": "Turkmenistan Manat",
    "country": "Turkmenistan"
  },
  {
    "currency_code": "TND",
    "currency_name": "Tunisian Dinar",
    "country": "Tunisia"
  },
  {
    "currency_code": "TOP",
    "currency_name": "Tongan Pa?anga",
    "country": "Tonga"
  },
  {
    "currency_code": "TRY",
    "currency_name": "Turkish Lira",
    "country": "Turkey"
  },
  {
    "currency_code": "TTD",
    "currency_name": "Trinidad and Tobago Dollar",
    "country": "Trinidad and Tobago"
  },
  {
    "currency_code": "TVD",
    "currency_name": "Tuvaluan Dollar",
    "country": "Tuvalu"
  },
  {
    "currency_code": "TWD",
    "currency_name": "New Taiwan Dollar",
    "country": "Taiwan"
  },
  {
    "currency_code": "TZS",
    "currency_name": "Tanzanian Shilling",
    "country": "Tanzania"
  },
  {
    "currency_code": "UAH",
    "currency_name": "Ukrainian Hryvnia",
    "country": "Ukraine"
  },
  {
    "currency_code": "UGX",
    "currency_name": "Ugandan Shilling",
    "country": "Uganda"
  },
  {
    "currency_code": "USD",
    "currency_name": "United States Dollar",
    "country": "United States"
  },
  {
    "currency_code": "UYU",
    "currency_name": "Uruguayan Peso",
    "country": "Uruguay"
  },
  {
    "currency_code": "UZS",
    "currency_name": "Uzbekistani So'm",
    "country": "Uzbekistan"
  },
  {
    "currency_code": "VES",
    "currency_name": "Venezuelan Bol�var Soberano",
    "country": "Venezuela"
  },
  {
    "currency_code": "VND",
    "currency_name": "Vietnamese ??ng",
    "country": "Vietnam"
  },
  {
    "currency_code": "VUV",
    "currency_name": "Vanuatu Vatu",
    "country": "Vanuatu"
  },
  {
    "currency_code": "WST",
    "currency_name": "Samoan T?l?",
    "country": "Samoa"
  },
  {
    "currency_code": "XAF",
    "currency_name": "Central African CFA Franc",
    "country": "CEMAC"
  },
  {
    "currency_code": "XCD",
    "currency_name": "East Caribbean Dollar",
    "country": "Organisation of Eastern Caribbean States"
  },
  {
    "currency_code": "XDR",
    "currency_name": "Special Drawing Rights",
    "country": "International Monetary Fund"
  },
  {
    "currency_code": "XOF",
    "currency_name": "West African CFA franc",
    "country": "CFA"
  },
  {
    "currency_code": "XPF",
    "currency_name": "CFP Franc",
    "country": "Collectivit�s d'Outre-Mer"
  },
  {
    "currency_code": "YER",
    "currency_name": "Yemeni Rial",
    "country": "Yemen"
  },
  {
    "currency_code": "ZAR",
    "currency_name": "South African Rand",
    "country": "South Africa"
  },
  {
    "currency_code": "ZMW",
    "currency_name": "Zambian Kwacha",
    "country": "Zambia"
  }
}
