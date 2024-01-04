import os
from dotenv import load_dotenv
import requests

load_dotenv()
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def construct_url(symbols, start_date, end_date, calculations):
    base_url = 'https://alphavantageapi.co/timeseries/analytics?'
    symbols_str = ','.join(symbols)
    calculations_str = ','.join(calculations)

    url = f'{base_url}SYMBOLS={symbols_str}&RANGE={start_date}&RANGE={end_date}&INTERVAL=DAILY&OHLC=close&CALCULATIONS={calculations_str}&apikey={ALPHA_VANTAGE_API_KEY}'
    return url

symbols = ['SPY']
start_date = '2014-01-01'
end_date = '2024-01-01'
calculations = ['MEAN', 'STDDEV(annualized=True)', 'MIN', 'MAX', 'MAX_DRAWDOWN']

url = construct_url(symbols, start_date, end_date, calculations)
r = requests.get(url)

data = r.json()
payload = data['payload']

print(payload)