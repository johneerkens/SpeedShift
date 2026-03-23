"""Core conversion logic shared by CLI, desktop GUI, and Android app."""

from __future__ import annotations

SPEED_UNITS_TO_MS: dict[str, float] = {
    "km/h": 0.277778,
    "mph": 0.44704,
    "m/s": 1.0,
    "knots": 0.514444,
    "ft/s": 0.3048,
    "cm/s": 0.01,
    "Mach (approx)": 343.0,
}


def convert_speed(value: float, from_unit: str, to_unit: str) -> float:
    """Convert ``value`` from ``from_unit`` to ``to_unit``.

    Raises:
        KeyError: If either unit is not supported.
    """
    value_ms = value * SPEED_UNITS_TO_MS[from_unit]
    return value_ms / SPEED_UNITS_TO_MS[to_unit]


def kmh_to_mph(kmh: float) -> float:
    """Legacy helper retained for CLI compatibility."""
    return convert_speed(kmh, "km/h", "mph")


def mph_to_kmh(mph: float) -> float:
    """Legacy helper retained for CLI compatibility."""
    return convert_speed(mph, "mph", "km/h")
