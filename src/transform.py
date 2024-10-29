import pandas as pd
from calculate import calculate_consumption


def transform(filename):
    """
    Calculate net export to Germany for DK1 and DK2 and its percentage of total annual energy consumption.

    Parameters:
    filename (str): The filename of the CSV file containing the data.

    Returns:
    dict: Dictionary containing the calculated results.
    """
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
