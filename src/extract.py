import requests
import pandas as pd
from config import BASE_URL


def extract(year):
    """Fetch data from the EnergiDataService API for a given year."""
    params = {
        "offset": 0,
        "start": f"{year}-01-01T00:00",
        "end": f"{year}-12-31T00:00",
        "sort": "Minutes5UTC DESC",
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    records = response.json().get("records", [])

    print(f"Extracted {len(records)} records.")
    return pd.DataFrame(records)
