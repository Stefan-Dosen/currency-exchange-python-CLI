#Currency Converter
A straightforward Python script that converts money from one currency to another using live rates from ExchangeRate-API.

#What it does
Fetches up-to-date exchange rates in real time

Converts any amount between your chosen currencies

Simple command-line interface, great for learning or quick conversions

#Requirements
Python 3 (tested on 3.8+)

requests library (pip install requests)

#How to run
Clone the repo:

git clone https://github.com/yourusername/currency-converter.git
cd currency-converter
Install dependencies:

pip install requests
Run the script:

currency_exchange.py
Follow the prompts to enter:

The currency you have (e.g., USD)

The amount to convert

The currency you want to convert to (e.g., EUR)

And voilà — you get your converted amount right away.

Example run

Enter currency being converted (eg. EUR): USD
Enter amount of money: 100
Enter currency to convert to (eg. EUR): EUR
100.0 USD is 91.23 EUR
#A couple of notes
This uses the free tier of ExchangeRate-API — replace the API key in the code with your own for better limits.

No fancy GUI, just simple and effective CLI. Perfect if you want to see how APIs work or need quick currency conversions.

License
MIT License
