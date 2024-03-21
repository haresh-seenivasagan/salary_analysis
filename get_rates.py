import requests
import pandas as pd

# Generate APP id from https://openexchangerates.org/account/app-ids and replace below
API_KEY = '583fa587182341dca7468e4414686316'
URL = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"

def fetch_conversion_rates():
    response = requests.get(URL)
    if response.status_code == 200:
        rates = response.json().get('rates', {})
        return rates
    else:
        print(f"Failed to fetch rates: {response.status_code}")
        return {}

def update_rates():
    rates = fetch_conversion_rates()
    if rates:
        rates_df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate to USD'])
        rates_df.to_csv('data/currency_conversion_rates.csv', index=False)
        print("Latest conversion rates saved to data/currency_conversion_rates.csv")
    else:
        print("No rates fetched.")

if __name__ == "__main__":
    update_rates()
