import pandas as pd

from modules import prices


class FakeTicker:
    """Ersetzt yfinance, damit die Tests ohne Internet laufen."""

    verlauf = pd.DataFrame({"Close": [10.0, 12.5]})

    def __init__(self, symbol):
        self.symbol = symbol

    def history(self, period):
        return self.verlauf


def test_letzter_schlusskurs(monkeypatch):
    monkeypatch.setattr(prices.yf, "Ticker", FakeTicker)
    assert prices.get_current_price("TEST") == 12.5


def test_ohne_daten_kommt_none(monkeypatch):
    class Leer(FakeTicker):
        verlauf = pd.DataFrame({"Close": []})

    monkeypatch.setattr(prices.yf, "Ticker", Leer)
    assert prices.get_current_price("TEST") is None
