import os
import pandas as pd


def load_portfolio():
    """Lädt das Portfolio aus der konfigurierten Excel-Datei."""

    datei = os.getenv(
        "PORTFOLIO_FILE",
        "portfolio_demo.xlsx"
    )

    df = pd.read_excel(datei)

    return df