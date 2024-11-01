import pandas as pd
from calculate import calculate_consumption
from concurrent.futures import ProcessPoolExecutor


def calculate_net_export(df, price_area):
    return df[df["PriceArea"] == price_area]["ExchangeGermany"].sum()


def calculate_total_consumption(df):
    return calculate_consumption(df)


def calculate_export_percentage(total_net_export, total_annual_consumption):
    return (
        (total_net_export / total_annual_consumption) * 100
        if total_annual_consumption
        else 0
    )


def calculate_production(df, column):
    return df[column].sum()


def calculate_production_wrapper(args):
    df, column = args
    return calculate_production(df, column)


def transform(filename):
    """
    Calculate various metrics for energy data.

    Parameters:
    filename (str): The filename of the CSV file containing the data.

    Returns:
    dict: Dictionary containing the calculated results.
    """
    df = pd.read_csv(filename)

    with ProcessPoolExecutor() as executor:
        net_exports = list(executor.map(calculate_net_export, [df, df], ["DK1", "DK2"]))
        total_net_export = sum(net_exports)
        total_annual_consumption = executor.submit(
            calculate_total_consumption, df
        ).result()
        export_percentage = executor.submit(
            calculate_export_percentage, total_net_export, total_annual_consumption
        ).result()

        production_columns = [
            "ProductionLt100MW",
            "ProductionGe100MW",
            "OffshoreWindPower",
            "OnshoreWindPower",
            "SolarPower",
        ]
        productions = list(
            executor.map(
                calculate_production_wrapper, [(df, col) for col in production_columns]
            )
        )

    return {
        "Net Export DK1 (MW)": net_exports[0],
        "Net Export DK2 (MW)": net_exports[1],
        "Total Net Export (MW)": total_net_export,
        "Export Percentage (%)": export_percentage,
        "Production < 100 MW (MW)": productions[0],
        "Production >= 100 MW (MW)": productions[1],
        "Offshore Wind Power (MW)": productions[2],
        "Onshore Wind Power (MW)": productions[3],
        "Solar Power (MW)": productions[4],
    }
