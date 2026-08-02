def calculate_position(kaufpreis, anzahl, aktueller_kurs):
    """
    Berechnet alle wichtigen Werte einer Position.
    """

    investiert = kaufpreis * anzahl
    aktueller_wert = aktueller_kurs * anzahl
    gewinn = aktueller_wert - investiert
    rendite = (gewinn / investiert) * 100

    return {
        "investiert": investiert,
        "aktueller_wert": aktueller_wert,
        "gewinn": gewinn,
        "rendite": rendite
    }