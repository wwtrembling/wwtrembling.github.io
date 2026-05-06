"""Programmatic SEO data for /convert/<from>-to-<to>/ pages.

Each pair defines an interactive single-pair unit converter page. Linear pairs
use a multiplicative `factor`; non-linear pairs (temperature) use a `formula`
key that names a JS function in the template.
"""

CONVERSION_PAIRS = [
    # length
    {
        'from': 'cm',
        'to': 'inches',
        'from_long': {'en': 'centimeters', 'ko': '센티미터'},
        'to_long': {'en': 'inches', 'ko': '인치'},
        'type': 'length',
        'mode': 'linear',
        'factor': 0.3937007874,
        'formula': 'inches = cm × 0.3937007874  (or cm ÷ 2.54)',
        'inverse_formula': 'cm = inches × 2.54',
        'precision': 4,
    },
    {
        'from': 'inches',
        'to': 'cm',
        'from_long': {'en': 'inches', 'ko': '인치'},
        'to_long': {'en': 'centimeters', 'ko': '센티미터'},
        'type': 'length',
        'mode': 'linear',
        'factor': 2.54,
        'formula': 'cm = inches × 2.54',
        'inverse_formula': 'inches = cm × 0.3937007874',
        'precision': 4,
    },
    {
        'from': 'meters',
        'to': 'feet',
        'from_long': {'en': 'meters', 'ko': '미터'},
        'to_long': {'en': 'feet', 'ko': '피트'},
        'type': 'length',
        'mode': 'linear',
        'factor': 3.2808398950,
        'formula': 'feet = meters × 3.2808398950',
        'inverse_formula': 'meters = feet × 0.3048',
        'precision': 4,
    },
    {
        'from': 'feet',
        'to': 'meters',
        'from_long': {'en': 'feet', 'ko': '피트'},
        'to_long': {'en': 'meters', 'ko': '미터'},
        'type': 'length',
        'mode': 'linear',
        'factor': 0.3048,
        'formula': 'meters = feet × 0.3048',
        'inverse_formula': 'feet = meters × 3.2808398950',
        'precision': 4,
    },
    {
        'from': 'km',
        'to': 'miles',
        'from_long': {'en': 'kilometers', 'ko': '킬로미터'},
        'to_long': {'en': 'miles', 'ko': '마일'},
        'type': 'length',
        'mode': 'linear',
        'factor': 0.6213711922,
        'formula': 'miles = km × 0.6213711922',
        'inverse_formula': 'km = miles × 1.609344',
        'precision': 4,
    },
    {
        'from': 'miles',
        'to': 'km',
        'from_long': {'en': 'miles', 'ko': '마일'},
        'to_long': {'en': 'kilometers', 'ko': '킬로미터'},
        'type': 'length',
        'mode': 'linear',
        'factor': 1.609344,
        'formula': 'km = miles × 1.609344',
        'inverse_formula': 'miles = km × 0.6213711922',
        'precision': 4,
    },
    # weight
    {
        'from': 'kg',
        'to': 'lbs',
        'from_long': {'en': 'kilograms', 'ko': '킬로그램'},
        'to_long': {'en': 'pounds', 'ko': '파운드'},
        'type': 'weight',
        'mode': 'linear',
        'factor': 2.2046226218,
        'formula': 'lbs = kg × 2.2046226218',
        'inverse_formula': 'kg = lbs × 0.45359237',
        'precision': 4,
    },
    {
        'from': 'lbs',
        'to': 'kg',
        'from_long': {'en': 'pounds', 'ko': '파운드'},
        'to_long': {'en': 'kilograms', 'ko': '킬로그램'},
        'type': 'weight',
        'mode': 'linear',
        'factor': 0.45359237,
        'formula': 'kg = lbs × 0.45359237',
        'inverse_formula': 'lbs = kg × 2.2046226218',
        'precision': 4,
    },
    # temperature
    {
        'from': 'celsius',
        'to': 'fahrenheit',
        'from_long': {'en': 'Celsius', 'ko': '섭씨'},
        'to_long': {'en': 'Fahrenheit', 'ko': '화씨'},
        'type': 'temperature',
        'mode': 'temp_c_to_f',
        'formula': '°F = (°C × 9/5) + 32',
        'inverse_formula': '°C = (°F − 32) × 5/9',
        'precision': 2,
    },
    {
        'from': 'fahrenheit',
        'to': 'celsius',
        'from_long': {'en': 'Fahrenheit', 'ko': '화씨'},
        'to_long': {'en': 'Celsius', 'ko': '섭씨'},
        'type': 'temperature',
        'mode': 'temp_f_to_c',
        'formula': '°C = (°F − 32) × 5/9',
        'inverse_formula': '°F = (°C × 9/5) + 32',
        'precision': 2,
    },
]


# Pretty input values for the SEO conversion table (10 rows).
TABLE_INPUT_VALUES = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
TABLE_INPUT_VALUES_TEMP = [-40, -20, 0, 10, 20, 25, 30, 37, 50, 100]


def convert(value, mode, factor=None):
    """Run a conversion. Returns a Python float."""
    if mode == 'linear':
        return value * factor
    if mode == 'temp_c_to_f':
        return (value * 9.0 / 5.0) + 32.0
    if mode == 'temp_f_to_c':
        return (value - 32.0) * 5.0 / 9.0
    raise ValueError(f"Unknown mode: {mode}")


def format_number(value, precision):
    """Trim trailing zeros to keep the table tidy."""
    s = f"{value:.{precision}f}"
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s if s else '0'
