import yfinance as yf

def get_current_price(symbol):
    """Liefert den aktuellen Kurs eines Symbols."""
    ticker = yf.Ticker(symbol)
    history = ticker.history(period="1d")

    if history.empty:
        return None

    return history["Close"].iloc[-1]