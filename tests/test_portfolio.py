from pathlib import Path

from modules.portfolio import load_portfolio

REPO = Path(__file__).resolve().parent.parent
SPALTEN = {"Name", "Typ", "Symbol", "Kaufpreis", "Anzahl"}


def test_standard_ist_die_demo_datei(monkeypatch):
    monkeypatch.chdir(REPO)
    monkeypatch.delenv("PORTFOLIO_FILE", raising=False)
    df = load_portfolio()
    assert SPALTEN <= set(df.columns)
    assert len(df) > 0


def test_demo_werte_sind_plausibel(monkeypatch):
    monkeypatch.chdir(REPO)
    monkeypatch.delenv("PORTFOLIO_FILE", raising=False)
    df = load_portfolio()
    assert (df["Kaufpreis"] > 0).all()
    assert (df["Anzahl"] > 0).all()
