"""
Functions used for creating links in test_main.py
"""
from constants import KEY


def api_coordinates_link(lat, lon):
    """
    Fucntion for creating a link to api,
    takes the KEY for api from constants.py

    :param lat: latitude of a city
    :param lon: longitude of a city
    :return: link to OpenWeather api
    :rtype: str
    """
    return f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}"


def api_city_link(city_name: str):
    """
    Fucntion for creating a link to api,
    takes the KEY for api from constants.py

    :param city_name: name of a city
    :return: link to OpenWeather api
    :rtype: str
    """
    return f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={KEY}"
