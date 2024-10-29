from config import EXPORT_STATEMENT
from extract import extract
from load import load
from transform import transform
from save_results import save_results
from ensure_directories import ensure_directories


def run(year):
    """
    Run the ELT pipeline: extract, load, and transform.

    Parameters:
    year (int): The year for which to run the ELT process.
    """
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
