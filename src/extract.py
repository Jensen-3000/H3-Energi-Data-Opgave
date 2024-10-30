import requests
import pandas as pd
from config import BASE_URL

import concurrent.futures


def extract(years):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_data_for_year, years))
    return pd.concat(results)


def fetch_data_for_year(year):
    params = {
        "offset": 0,
        "start": f"{year}-01-01T00:00",
        "end": f"{year}-12-31T00:00",
        "sort": "Minutes5UTC DESC",
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    records = response.json().get("records", [])
    print(f"Extracted {len(records)} records for {year}.")
    return pd.DataFrame(records)
