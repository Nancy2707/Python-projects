import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.openexchangerates.org/v6/latest?app_id=YOUR_APP_ID"
    response = requests.get(url)
    data = response.json()

    conversion_rate = data['rates'][to_currency] / data['rates'][from_currency]
    converted_amount = amount * conversion_rate

    return converted_amount

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ")
to_currency = input("Enter the currency to convert to: ")

print("Converted amount: ", convert_currency(amount, from_currency, to_currency))