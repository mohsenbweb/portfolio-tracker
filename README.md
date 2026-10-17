# 📊 Portfolio Tracker

Ein Python-basierter Portfolio Tracker zur Verwaltung und Analyse eines Wertpapierportfolios mit Aktien, ETFs und Kryptowährungen.

Das Projekt verwendet aktuelle Marktdaten und stellt wichtige Portfolio-Kennzahlen übersichtlich in einem Streamlit-Dashboard dar.

## ✨ Funktionen

- 📊 Portfolio-Dashboard mit Streamlit
- 📈 Aktien, ETFs und Kryptowährungen verwalten
- 🔄 Aktuelle Kurse über Yahoo Finance (`yfinance`)
- 💰 Investiertes Kapital und aktueller Portfoliowert
- 📈 Gewinn und Verlust automatisch berechnen
- 📉 Rendite in Prozent berechnen
- 🟢 Positive und 🔴 negative Entwicklungen farblich darstellen
- 📊 Portfolio-Verteilung nach Anlageklasse
- 📈 Grafische Darstellung der Portfolio-Verteilung mit Plotly
- 📗 Excel-basierte Portfolio-Daten
- 🔐 Trennung von privaten Portfolio-Daten und öffentlichen Demo-Daten
- 🧩 Modulare Projektstruktur für zukünftige Erweiterungen

## 🖥️ Dashboard

Das Dashboard zeigt unter anderem:

- Gesamtportfolio
- Investiertes Kapital
- Aktuellen Portfoliowert
- Gewinn / Verlust
- Rendite
- Aktien
- ETFs
- Kryptowährungen
- Einzelne Portfolio-Positionen
- Portfolio-Verteilung nach Anlageklasse

## 🛠️ Verwendete Technologien

- **Python 3**
- **Streamlit**
- **Pandas**
- **yfinance**
- **OpenPyXL**
- **Plotly**
- **Git & GitHub**

## 🚀 Installation und Nutzung

### Voraussetzungen

- Python 3
- Git

### Demo starten

```bash
git clone https://github.com/mohsenbweb/portfolio-tracker.git
cd portfolio-tracker
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run dashboard.py
```

Das Dashboard öffnet sich im Browser (meist unter `http://localhost:8501`). Es zeigt **fiktive Demo-Daten** aus `portfolio_demo.xlsx` und `portfolio_history_demo.csv`. Die Kurse werden live von Yahoo Finance geladen, dafür ist eine Internetverbindung nötig.

### Eigenes Portfolio verwenden

1. Lege im Projektordner eine Excel-Datei `portfolio.xlsx` an. Am einfachsten kopierst du `portfolio_demo.xlsx` und ersetzt die Zeilen. Die Datei braucht diese Spalten:

| Spalte | Bedeutung | Beispiel |
|---|---|---|
| Name | frei wählbar | Bitcoin |
| Typ | `Aktie`, `ETF` oder `Krypto` | Krypto |
| Symbol | Kürzel bei Yahoo Finance | `BTC-EUR`, `SAP.DE` |
| Kaufpreis | Kaufpreis pro Stück in Euro | 25000 |
| Anzahl | Stückzahl | 0.5 |

2. Starte das Dashboard mit deinen Dateien:

```bash
PORTFOLIO_FILE=portfolio.xlsx PORTFOLIO_HISTORY_FILE=portfolio_history.csv streamlit run dashboard.py
```

Unter Windows (PowerShell):

```powershell
$env:PORTFOLIO_FILE="portfolio.xlsx"; $env:PORTFOLIO_HISTORY_FILE="portfolio_history.csv"; streamlit run dashboard.py
```

**Hinweise**

- `portfolio.xlsx` und `portfolio_history.csv` stehen in der `.gitignore`. Deine eigenen Daten werden dadurch nicht versehentlich ins Repository übernommen.
- Die History-Datei wird automatisch angelegt und höchstens einmal pro Stunde ergänzt.
- Yahoo Finance liefert Kurse in der Währung der jeweiligen Börse. Für eine Anzeige in Euro nimm Symbole mit Euro-Notierung, zum Beispiel `BTC-EUR` statt `BTC-USD`.
- Die Demo-Daten sind frei erfunden. Das Projekt ist ein Lern- und Portfolioprojekt und keine Anlage- oder Steuerberatung.

## 📁 Projektstruktur

```text
portfolio-tracker/
│
├── app.py
├── dashboard.py
├── requirements.txt
├── README.md
├── portfolio_demo.xlsx
│
├── modules/
│   ├── calculations.py
│   ├── portfolio.py
│   └── prices.py
│
└── .gitignore
```
