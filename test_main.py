from http import HTTPStatus

import pytest
import requests
from jsonschema import validate

from constants import LONDON, AMSTERDAM, BOMBAY, CITY_NAMES, CITY_NAMES_DIFFERENT_CASES, SCHEMA, api_coordinates_link, \
    api_city_link


# TODO
# single request for whole test where possible?

# test using lat and lon
class TestApiCoordinates:

    @staticmethod
    @pytest.mark.parametrize("lat,lon", [(LONDON["LAT"], LONDON["LON"]), (AMSTERDAM["LAT"], AMSTERDAM["LON"]),
                                         (BOMBAY["LAT"], BOMBAY["LON"])])
    def test_coordinates(lat, lon):
        response = requests.get(api_coordinates_link(lat, lon))
        assert response.status_code == HTTPStatus.OK


class TestApiCityName:
    # test using city names

    @staticmethod
    @pytest.mark.parametrize("city_name", [CITY_NAMES[0], CITY_NAMES[1], CITY_NAMES[2]])
    def test_city(city_name):
        response = requests.get(api_city_link(city_name))
        assert response.status_code == HTTPStatus.OK

    @staticmethod
    @pytest.mark.parametrize("city_name", [CITY_NAMES_DIFFERENT_CASES[0], CITY_NAMES_DIFFERENT_CASES[1],
                                           CITY_NAMES_DIFFERENT_CASES[2]])
    def test_city_cases(city_name):
        response = requests.get(api_city_link(city_name))
        assert response.status_code == HTTPStatus.OK


class TestApiError:

    def test_error_coordinates_letter(self):
        # generate random letters?
        response = requests.get(api_coordinates_link("a", "b"))
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_error_coordinates_number(self):
        response = requests.get(api_coordinates_link("c", "d"))
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_error_city_letter(self):
        response = requests.get(api_city_link("a"))
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_error_city_number(self):
        response = requests.get(api_city_link("2"))
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestApiErrorParametrized:

    @staticmethod
    @pytest.mark.parametrize("lat,lon", [("a", "b"), ("c", "d")])
    def test_coordinates(lat, lon):
        response = requests.get(api_coordinates_link(lat, lon))
        assert response.status_code == HTTPStatus.BAD_REQUEST

    @staticmethod
    @pytest.mark.parametrize("city_name", ["a", "1"])
    def test_city(city_name):
        response = requests.get(api_city_link(city_name))
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestApiResponse:

    @staticmethod
    @pytest.fixture(params=[(LONDON["LAT"], LONDON["LON"]), (AMSTERDAM["LAT"], AMSTERDAM["LON"]),
                            (BOMBAY["LAT"], BOMBAY["LON"])])
    def response(request):
        return requests.get(api_coordinates_link(request.param[0], request.param[1]))

    @staticmethod
    def test_response_types(response):
        validate(instance=response.json(), schema=SCHEMA)
