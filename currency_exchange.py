import requests
import json

input_currency = input("Enter currency being coverted (eg. EUR)")

url = 'https://v6.exchangerate-api.com/v6/14c86bdf82929ac15c393457/latest/' + input_currency
response = requests.get(url)
data = response.json()

input_value = float(input("Enter amount of money"))

output_currency = input("Enter currency to cover to (eg. EUR)")

output_multiplier = data["conversion_rates"].get(output_currency)

output_value = input_value * output_multiplier

print(f"{output_value}{output_currency} ")