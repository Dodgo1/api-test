"""
Functions used for creating links in test_main.py
"""
from constants import KEY


def api_coordinates_link(lat, lon):  # :int :int
    return f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}"


def api_city_link(city_name: str):
    return f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={KEY}"
