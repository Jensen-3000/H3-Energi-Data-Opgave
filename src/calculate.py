def calculate_consumption(df):
    """
    Calculate total annual energy consumption from the DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing energy data.

    Returns:
    float: Total annual energy consumption.
    """
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
