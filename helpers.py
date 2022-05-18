"""
Functions used for creating links in test_main.py
"""
import os

from dotenv import load_dotenv
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from pytest import fail

load_dotenv()

KEY = os.environ["KEY"]


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


def api_city_link(city_name):
    """
    Fucntion for creating a link to api,
    takes the KEY for api from constants.py

    :param city_name: name of a city
    :return: link to OpenWeather api
    :rtype: str
    """
    return f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={KEY}"


def validate_response_json(response, schema):
    """
    Function throws a pytest fail if response doesn't fit the schema

    :param response: response object - requests.Response
    :param schema: Json schema for validating
    :return: pytest fail
    """
    try:
        validate(instance=response.json(), schema=schema)
    except ValidationError:
        return fail("Validation Failed")
