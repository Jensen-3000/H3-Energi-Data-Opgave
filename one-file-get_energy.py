import os
import requests
import pandas as pd


# Configuration settings
BASE_URL = "https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime"
OUTPUT_DIR = "data"
RESULTS_DIR = "results"
EXPORT_STATEMENT = (
    "A positive exchange indicates import of electricity to Denmark, "
    "while a negative exchange indicates export of electricity from Denmark."
)


def ensure_directories():
    """Ensure that output and results directories exist."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)


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


def load(df, year):
    """Save the DataFrame to a CSV file."""
    filename = os.path.join(OUTPUT_DIR, f"electricity_data_{year}.csv")
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}.")
    return filename


def calculate_consumption(df):
    """Calculate total annual energy consumption from the DataFrame."""
    consumption_cols = [
        "ProductionLt100MW",
        "ProductionGe100MW",
        "OffshoreWindPower",
        "OnshoreWindPower",
        "SolarPower",
        "ExchangeGermany",
        "ExchangeNorway",
        "ExchangeSweden",
        "ExchangeNetherlands",
        "BornholmSE4",
    ]
    return df[consumption_cols].sum().sum()


def transform(filename):
    """Calculate net export to Germany for DK1 and DK2 and its percentage of total annual energy consumption."""
    df = pd.read_csv(filename)

    # Calculate net exports for DK1 and DK2
    net_export_dk1 = df[df["PriceArea"] == "DK1"]["ExchangeGermany"].sum()
    net_export_dk2 = df[df["PriceArea"] == "DK2"]["ExchangeGermany"].sum()
    total_net_export = net_export_dk1 + net_export_dk2

    # Calculate total annual energy consumption
    total_annual_consumption = calculate_consumption(df)

    # Calculate export percentage
    export_percentage = (
        (total_net_export / total_annual_consumption) * 100
        if total_annual_consumption
        else 0
    )

    return {
        "Net Export DK1 (MW)": net_export_dk1,
        "Net Export DK2 (MW)": net_export_dk2,
        "Total Net Export (MW)": total_net_export,
        "Export Percentage (%)": export_percentage,
    }


def save_results(results, year):
    """Save results to a text file."""
    output_filename = os.path.join(RESULTS_DIR, f"results_{year}.txt")
    with open(output_filename, "w") as f:
        f.write("Electricity Export Analysis\n")
        f.write(f"Year: {year}\n")
        f.write("-----------------------------\n")
        f.write(f"{EXPORT_STATEMENT}\n")
        f.write("-----------------------------\n")
        for key, value in results.items():
            f.write(f"{key}: {value:.2f}\n")
    print(f"Results saved to {output_filename}.")


def run(year):
    """Run the ELT pipeline: extract, load, and transform."""
    print(f"Starting ELT process for the year {year}...")

    # Ensure directories exist
    ensure_directories()

    # Extract data
    df = extract(year)

    # Load data
    filename = load(df, year)

    # Transform data
    result = transform(filename)

    # Save results
    save_results(result, year)

    print(f"ELT process for the year {year} completed.")
    print()
    print(EXPORT_STATEMENT)
    print("Final Results:")
    for key, value in result.items():
        print(f"{key}: {value:.2f}")


if __name__ == "__main__":
    year = 2024
    run(year)
