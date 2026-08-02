import pandas as pd

def load_portfolio():
    """Lädt das Portfolio aus der Excel-Datei."""
    df = pd.read_excel("portfolio.xlsx")
    return df