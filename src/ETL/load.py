import os
from config import OUTPUT_DIR


def load(df, year):
    """
    Save the DataFrame to a CSV file.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data to be saved.
    year (int): The year for which the data was fetched.

    Returns:
    str: The filename of the saved CSV file.
    """
    filename = os.path.join(OUTPUT_DIR, f"electricity_data_{year}.csv")
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}.")
    return filename
