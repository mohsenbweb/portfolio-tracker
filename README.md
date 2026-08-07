# Portfolio Tracker

Ein Python-basierter Portfolio Tracker für Aktien, ETFs und Kryptowährungen mit Live-Kursen.

## Funktionen

- Aktien, ETFs und Kryptowährungen verwalten
- Live-Kurse über **Yahoo Finance (yfinance)**
- Gewinn und Verlust automatisch berechnen
- Rendite in Prozent anzeigen
- Portfolio als Excel-Bericht exportieren
- Modulare Projektstruktur für einfache Erweiterungen

## Verwendete Technologien

- Python 3
- pandas
- yfinance
- openpyxl
- Streamlit (geplant)
- Plotly (geplant)
- Git & GitHub

## Projektstruktur

```text
portfolio-tracker/
│
├── app.py
├── requirements.txt
├── README.md
├── portfolio.xlsx
├── modules/
│   ├── calculations.py
│   ├── portfolio.py
│   └── prices.py
└── .gitignore
```

## Installation

Repository klonen:

```bash
git clone https://github.com/mohsenbweb/portfolio-tracker.git
cd portfolio-tracker
```

Virtuelle Umgebung erstellen:

```bash
python3 -m venv .venv
```

Virtuelle Umgebung aktivieren:

Linux/macOS

```bash
source .venv/bin/activate
```

Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Pakete installieren:

```bash
pip install -r requirements.txt
```

Programm starten:

```bash
python app.py
```

## Roadmap

- [x] Portfolio aus Excel laden
- [x] Live-Kurse abrufen
- [x] Gewinn und Verlust berechnen
- [x] Excel-Bericht erzeugen
- [ ] Streamlit-Weboberfläche
- [ ] Diagramme mit Plotly
- [ ] SQLite-Datenbank
- [ ] Kauf- und Verkaufshistorie
- [ ] Dashboard
- [ ] Cloud Deployment

## Lizenz

Dieses Projekt dient als Lern- und Demonstrationsprojekt.
