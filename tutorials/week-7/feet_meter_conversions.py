"""
This module contains the functions for converting between feet and meters.
"""


def feet_to_meters(feet: float):
    """
    This function accepts a feet parameter, then calculates and returns the equivalent in meters.
    """
    meters = round(float(feet * 0.3048), 2)

    return meters


def meters_to_feet(meters: float):
    """
    This function accepts a meter parameter, then calculates and returns the equivalent in feet.
    """
    feet = round(float(meters / 0.3048), 2)

    return feet
