import pandas as pd

from modules.portfolio import load_portfolio
from modules.prices import get_current_price
from modules.calculations import calculate_position

# Portfolio laden
portfolio = load_portfolio()

print("\n=== Mein Portfolio ===\n")
print(portfolio)

# Liste für die Ergebnisse
results = []

# Summen
gesamt_investiert = 0
gesamt_wert = 0

print("\n=== Portfolio-Auswertung ===\n")

# Alle Positionen durchlaufen
for _, row in portfolio.iterrows():

    kurs = get_current_price(row["Symbol"])

    if kurs is None:
        print(f"{row['Name']}: Kein Kurs verfügbar")
        continue

    daten = calculate_position(
        row["Kaufpreis"],
        row["Anzahl"],
        kurs
    )

    # Summen berechnen
    gesamt_investiert += daten["investiert"]
    gesamt_wert += daten["aktueller_wert"]

    # Ergebnisse für die Tabelle speichern
    results.append({
        "Name": row["Name"],
        "Typ": row["Typ"],
        "Symbol": row["Symbol"],
        "Kaufpreis (€)": row["Kaufpreis"],
        "Aktueller Kurs (€)": round(kurs, 2),
        "Anzahl": row["Anzahl"],
        "Investiert (€)": round(daten["investiert"], 2),
        "Aktueller Wert (€)": round(daten["aktueller_wert"], 2),
        "Gewinn (€)": round(daten["gewinn"], 2),
        "Rendite (%)": round(daten["rendite"], 2)
    })

# DataFrame erzeugen
ergebnis = pd.DataFrame(results)

# Tabelle ausgeben
print("\n=== Portfolio ===\n")
print(ergebnis)

# Excel-Datei speichern
ergebnis.to_excel("portfolio_report.xlsx", index=False)

print("\nPortfolio-Bericht wurde gespeichert.")
print("Datei: portfolio_report.xlsx")

# Gesamtwerte berechnen
gesamt_gewinn = gesamt_wert - gesamt_investiert

# Zusammenfassung ausgeben
print("\n==============================")
print("Portfolio-Zusammenfassung")
print("==============================")

print(f"Gesamt investiert: {gesamt_investiert:.2f} €")
print(f"Gesamtwert:        {gesamt_wert:.2f} €")
print(f"Gesamtgewinn:      {gesamt_gewinn:.2f} €")