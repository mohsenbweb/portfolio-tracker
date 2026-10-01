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
