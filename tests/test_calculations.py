import pytest

from modules.calculations import calculate_position


def test_gewinn_und_rendite():
    erg = calculate_position(kaufpreis=10, anzahl=5, aktueller_kurs=12)
    assert erg["investiert"] == pytest.approx(50)
    assert erg["aktueller_wert"] == pytest.approx(60)
    assert erg["gewinn"] == pytest.approx(10)
    assert erg["rendite"] == pytest.approx(20)


def test_verlust():
    erg = calculate_position(20, 2, 15)
    assert erg["gewinn"] == pytest.approx(-10)
    assert erg["rendite"] == pytest.approx(-25)


def test_bruchteile_wie_bei_krypto():
    erg = calculate_position(100, 0.5, 150)
    assert erg["investiert"] == pytest.approx(50)
    assert erg["gewinn"] == pytest.approx(25)
    assert erg["rendite"] == pytest.approx(50)


def test_rendite_ohne_einsatz():
    """Gratis-Position: Kaufpreis 0 darf nicht zu einer Division durch 0 führen."""
    erg = calculate_position(0, 3, 10)
    assert erg["investiert"] == 0
    assert erg["gewinn"] == pytest.approx(30)
    assert erg["rendite"] == 0
