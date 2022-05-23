"""
Pytest file for testing https://openweathermap.org/api

Uses constants.py for city_values, api_key, coordinates
helpers.py contains functions for creating links using values mentioned above

"""

from http import HTTPStatus

import pytest
import requests

from constants import LONDON, AMSTERDAM, BOMBAY, CITY_NAMES, CITY_NAMES_DIFFERENT_CASES
from helpers import api_coordinates_link, api_city_link, validate_response_json
from schema import SCHEMA_COORDINATES, SCHEMA_CITY_NAME


# test using lat and lon
class TestApiCoordinates:
    """
    Test api using coordinates of cities listed constants.py
    pytest.mark.parametrize takes a list containing latitude and longitude
    """

    @staticmethod
    @pytest.mark.parametrize("lat,lon", [(LONDON["LAT"], LONDON["LON"]),
                                         (AMSTERDAM["LAT"], AMSTERDAM["LON"]),
                                         (BOMBAY["LAT"], BOMBAY["LON"])])
    def test_using_coordinates(lat, lon):
        """
        :param lat: latitude of the city
        :param lon: longitude of the city
        Checks if the HTTP_response.code == 400
        """
        response = requests.get(api_coordinates_link(lat, lon))

        validate_response_json(response, SCHEMA_COORDINATES)

        assert response.status_code == HTTPStatus.OK


# test using city names
class TestApiCityName:
    """
    Test api using city names
    pytest.mark.parametrize takes a string which is a city name
    """

    @staticmethod
    @pytest.mark.parametrize("city_name", [CITY_NAMES[0], CITY_NAMES[1], CITY_NAMES[2]])
    def test_using_city_name(city_name):
        """
        Test api using city names
        :param city_name: a city name provided by pytest
        pytest.mark.parametrize takes a string which is a city name
        Checks if the HTTP_response.code == 400
        """
        response = requests.get(api_city_link(city_name))

        validate_response_json(response, SCHEMA_CITY_NAME)

        assert response.status_code == HTTPStatus.OK

    @staticmethod
    @pytest.mark.parametrize("city_name", [CITY_NAMES_DIFFERENT_CASES[0],
                                           CITY_NAMES_DIFFERENT_CASES[1],
                                           CITY_NAMES_DIFFERENT_CASES[2]])
    def test_city_lower_and_upper_cases(city_name):
        """
        Test if api distinguishes between lowercase letters and uppercase
        :param city_name: city name with uppercase and lowercase letters
        Checks if the HTTP_response.code == 400
        """
        response = requests.get(api_city_link(city_name))

        validate_response_json(response, SCHEMA_CITY_NAME)

        assert response.status_code == HTTPStatus.OK


class TestApiErrorParametrized:
    """
    Test if api responds with adequate error type
    When letters are used in place of coordinates it should respond = BAD_REQUEST[400]
    When a number or an incorrect city is used
    instead of a correct city name respond = NOT_FOUND[400}
    """

    @staticmethod
    @pytest.mark.parametrize("lat,lon", [("a", "b"), ("c", "d")])
    def test_coordinates(lat, lon):
        """
        Letter:list(char,char) is used instead of coordinates:list(int,int)
        :return:is the HTTP_response.code == 400
        """
        response = requests.get(api_coordinates_link(lat, lon))

        # no validation cause of error testing

        assert response.status_code == HTTPStatus.BAD_REQUEST

    @staticmethod
    @pytest.mark.parametrize("city_name", ["a", "1"])
    def test_city(city_name):
        """
        Letter and a number is used instead of proper name of a city
        :return:is the HTTP_response.code == 400
        """
        response = requests.get(api_city_link(city_name))

        # no validation cause of error testing

        assert response.status_code == HTTPStatus.NOT_FOUND


class TestApiResponse:
    """
    Test for validating json response
    Checks if json has all the attributes and proper data types
    """

    # fixture runs multiple times every function which uses it
    @staticmethod
    @pytest.fixture(params=[(LONDON["LAT"], LONDON["LON"]), (AMSTERDAM["LAT"], AMSTERDAM["LON"]),
                            (BOMBAY["LAT"], BOMBAY["LON"])])
    def response_coordinates(request):
        """
        Pytest fixture, can be used in multiple tests
        If used, the test will run as many times as the fixture has parameters
        :param request: list(latitude:int,longitude:int) - latitude and longitude of a city
        assured by pytest.fixture-params, accessible by request.params
        :return: response object
        :rtype: requests.Response
        """
        return requests.get(api_coordinates_link(request.param[0], request.param[1]))

    @staticmethod
    @pytest.fixture(params=[CITY_NAMES[0], CITY_NAMES[1], CITY_NAMES[2]])
    def response_city_name(request):
        """
        Pytest fixture, can be used in multiple tests
        If used, the test will run as many times as the fixture has parameters
        :param request: name of a city
        assured by pytest.fixture-params, accessible by request.params
        :return: response object
        :rtype: requests.Response
        """
        return requests.get(api_city_link(request.param))

    @staticmethod
    def test_validate_json_response_coordinates(response_coordinates):
        """

        :param response_coordinates: pytest fixture, response object

        Tries to catch a ValidationError, if error throw pytest fail
        """

        validate_response_json(response_coordinates, SCHEMA_COORDINATES)
        assert response_coordinates.status_code == HTTPStatus.OK

    @staticmethod
    def test_validate_json_response_city_name(response_city_name):
        """

        :param response_city_name: pytest fixture, response object

        Tries to catch a ValidationError, if error throw pytest fail
        """

        validate_response_json(response_city_name, SCHEMA_CITY_NAME)
        assert response_city_name.status_code == HTTPStatus.OK
