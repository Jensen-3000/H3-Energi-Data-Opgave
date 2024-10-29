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
