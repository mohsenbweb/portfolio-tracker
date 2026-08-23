import streamlit as st
import pandas as pd
import plotly.express as px
import os

from modules.portfolio import load_portfolio
from modules.prices import get_current_price
from modules.calculations import calculate_position
from datetime import datetime


st.set_page_config(
    page_title="Portfolio Tracker",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
/* Überschriften */
h3 {
    font-size: 1.25rem !important;
}

h4 {
    font-size: 1.05rem !important;
}

/* Metric-Werte */
[data-testid="stMetricValue"] {
    font-size: 1.45rem !important;
}

/* Metric-Beschriftungen */
[data-testid="stMetricLabel"] {
    font-size: 0.85rem !important;
}
</style>
""", unsafe_allow_html=True)

def format_gewinn(value):
    if value > 0:
        return f"+{value:,.2f} €"
    elif value < 0:
        return f"{value:,.2f} €"
    return "0,00 €"

def farbe_gewinn(value):
    if value > 0:
        return "color: green"
    elif value < 0:
        return "color: red"
    return ""


def farbe_rendite(value):
    if value > 0:
        return "color: green"
    elif value < 0:
        return "color: red"
    return ""

st.title("📈 Portfolio Tracker")

st.markdown("### Mein Portfolio")


# Portfolio laden
portfolio = load_portfolio()

results = []

gesamt_investiert = 0
gesamt_wert = 0


# Live-Kurse und Berechnungen
for _, row in portfolio.iterrows():

    kurs = get_current_price(row["Symbol"])

    if kurs is None:
        continue

    daten = calculate_position(
        row["Kaufpreis"],
        row["Anzahl"],
        kurs
    )

    gesamt_investiert += daten["investiert"]
    gesamt_wert += daten["aktueller_wert"]

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


ergebnis = pd.DataFrame(results)

# Portfolio-Verteilung nach Typ
verteilung = (
    ergebnis.groupby("Typ")["Aktueller Wert (€)"]
    .sum()
    .reset_index()
)

# Kennzahlen

gesamt_gewinn = gesamt_wert - gesamt_investiert

rendite = 0

if gesamt_investiert > 0:
    rendite = (gesamt_gewinn / gesamt_investiert) * 100


# Portfolio-Wert speichern

history_file = "portfolio_history.csv"

neuer_eintrag = pd.DataFrame([{
    "Datum": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Investiert (€)": round(gesamt_investiert, 2),
    "Portfolio-Wert (€)": round(gesamt_wert, 2),
    "Gewinn (€)": round(gesamt_gewinn, 2)
}])


if os.path.exists(history_file):

    historie = pd.read_csv(history_file)

    # Prüfen, wann zuletzt gespeichert wurde
    letzter_eintrag = historie.iloc[-1]

    letzter_zeitpunkt = pd.to_datetime(
        letzter_eintrag["Datum"]
    )

    jetzt = datetime.now()

    minuten_seit_letztem_eintrag = (
        jetzt - letzter_zeitpunkt
    ).total_seconds() / 60

    # Nur speichern, wenn mindestens 60 Minuten vergangen sind
    if minuten_seit_letztem_eintrag >= 60:

        historie = pd.concat(
            [historie, neuer_eintrag],
            ignore_index=True
        )

        historie.to_csv(
            history_file,
            index=False
        )

else:

    neuer_eintrag.to_csv(
        history_file,
        index=False
    )





# Gesamtkennzahlen
st.subheader("💰 Gesamtportfolio")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Investiert",
    f"{gesamt_investiert:,.2f} €"
)

col2.metric(
    "Aktueller Wert",
    f"{gesamt_wert:,.2f} €"
)

col3.metric(
    "Gewinn / Verlust",
    format_gewinn(gesamt_gewinn)
)

col4.metric(
    "Rendite",
    f"{rendite:+.2f} %"
)

st.divider()


# Summen nach Asset-Typ
summen = (
    ergebnis
    .groupby("Typ")[[
        "Investiert (€)",
        "Aktueller Wert (€)",
        "Gewinn (€)"
    ]]
    .sum()
)


# Kategorien anzeigen
st.markdown("### 📊 Aufteilung nach Anlageklasse")


def zeige_anlageklasse(titel, typ):
    st.markdown(f"#### {titel}")

    if typ not in summen.index:
        st.info(f"Keine Positionen für {titel} vorhanden.")
        return

    investiert = summen.loc[typ, "Investiert (€)"]
    wert = summen.loc[typ, "Aktueller Wert (€)"]
    gewinn = summen.loc[typ, "Gewinn (€)"]

    rendite_typ = 0

    if investiert > 0:
        rendite_typ = (gewinn / investiert) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Investiert",
        f"{investiert:,.2f} €"
    )

    col2.metric(
        "Aktueller Wert",
        f"{wert:,.2f} €"
    )

    col3.metric(
        "Gewinn / Verlust",
        format_gewinn(gewinn)
    )

    col4.metric(
        "Rendite",
        f"{rendite_typ:+.2f} %"
    )


zeige_anlageklasse("📈 Aktien", "Aktie")

st.divider()

zeige_anlageklasse("🌍 ETFs", "ETF")

st.divider()

zeige_anlageklasse("🪙 Kryptowährungen", "Krypto")

st.divider()

# Portfolio-Tabelle

st.subheader("📊 Positionen")


styled_ergebnis = (
    ergebnis.style
    .map(farbe_gewinn, subset=["Gewinn (€)"])
    .map(farbe_rendite, subset=["Rendite (%)"])
    .format({
        "Kaufpreis (€)": "{:,.2f} €",
        "Aktueller Kurs (€)": "{:,.2f} €",
        "Investiert (€)": "{:,.2f} €",
        "Aktueller Wert (€)": "{:,.2f} €",
        "Gewinn (€)": "{:+,.2f} €",
        "Rendite (%)": "{:+.2f} %"
    })
)


st.dataframe(
    styled_ergebnis,
    use_container_width=True,
    hide_index=True
)


# Portfolio-Verteilung

st.subheader("📊 Portfolio-Verteilung")

fig = px.pie(
    verteilung,
    names="Typ",
    values="Aktueller Wert (€)",
    hole=0.4
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "Wert: %{value:,.2f} €<br>"
        "Anteil: %{percent}"
        "<extra></extra>"
    )
)

fig.update_layout(
    showlegend=True,
    margin=dict(t=20, b=20, l=20, r=20)
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# Historische Portfolioentwicklung

st.subheader("📈 Portfolioentwicklung")

history_file = "portfolio_history.csv"

if os.path.exists(history_file):

    historie = pd.read_csv(history_file)

    historie["Datum"] = pd.to_datetime(
        historie["Datum"]
    )

    # Zeitraum auswählen
    zeitraum = st.radio(
        "Zeitraum",
        ["7 Tage", "30 Tage", "3 Monate", "1 Jahr", "Alles"],
        horizontal=True
    )

    jetzt = pd.Timestamp.now()

    if zeitraum == "7 Tage":
        startdatum = jetzt - pd.Timedelta(days=7)

    elif zeitraum == "30 Tage":
        startdatum = jetzt - pd.Timedelta(days=30)

    elif zeitraum == "3 Monate":
        startdatum = jetzt - pd.Timedelta(days=90)

    elif zeitraum == "1 Jahr":
        startdatum = jetzt - pd.Timedelta(days=365)

    else:
        startdatum = historie["Datum"].min()

    historie_gefiltert = historie[
        historie["Datum"] >= startdatum
    ]

    fig_history = px.line(
        historie_gefiltert,
        x="Datum",
        y=["Portfolio-Wert (€)", "Investiert (€)"],
        markers=True
    )

    fig_history.update_layout(
    xaxis_title="Datum",
    yaxis_title="Euro (€)",
    legend_title="",
    margin=dict(
        t=20,
        b=20,
        l=20,
        r=20
    )
)

    st.plotly_chart(
        fig_history,
        use_container_width=True
    )

else:

    st.info(
        "Noch keine historischen Daten vorhanden."
    )