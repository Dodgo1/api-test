from http import HTTPStatus

import pytest
import requests
from jsonschema import validate

from constants import Key, LONDON, AMSTERDAM, BOMBAY, CITY_NAMES, CITY_NAMES_DIFFERENT_CASES,SCHEMA


# test using lat and lon
class TestApiCoordinates:

    @staticmethod
    @pytest.mark.parametrize("LAT,LON", [(LONDON["LAT"], LONDON["LON"]), (AMSTERDAM["LAT"], AMSTERDAM["LON"]),
                                         (BOMBAY["LAT"], BOMBAY["LON"])])
    def test_coordinates(LAT, LON):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={Key}")
        assert response.status_code == HTTPStatus.OK


class TestApiCityName:
    # test using city names

    @staticmethod
    @pytest.mark.parametrize("city_name", [CITY_NAMES[0], CITY_NAMES[1], CITY_NAMES[2]])
    def test_city(city_name):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
        assert response.status_code == HTTPStatus.OK

    @staticmethod
    @pytest.mark.parametrize("city_name", [CITY_NAMES_DIFFERENT_CASES[0], CITY_NAMES_DIFFERENT_CASES[1],
                                           CITY_NAMES_DIFFERENT_CASES[2]])
    def test_city_cases(city_name):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
        assert response.status_code == HTTPStatus.OK


class TestApiError:

    def test_coordinates_letter(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={'a'}&lon={'b'}&appid={Key}")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_coordinates_number(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={'d'}&lon={'f'}&appid={Key}")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_city_letter(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={'a'}&appid={Key}")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_city_number(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={'1'}&appid={Key}")
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestApiErrorParametrized:

    @staticmethod
    @pytest.mark.parametrize("lat,lon", [("a", "b"), ("c", "d")])
    def test_coordinates(lat, lon):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}")
        assert response.status_code == HTTPStatus.BAD_REQUEST

    @staticmethod
    @pytest.mark.parametrize("city_name", ["a", "1"])
    def test_city(city_name):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestApiResponse:

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={'10'}&lon={'25'}&appid={Key}")

    @pytest.mark.parametrize("LAT,LON", [(LONDON["LAT"], LONDON["LON"]), (AMSTERDAM["LAT"], AMSTERDAM["LON"]),
                                         (BOMBAY["LAT"], BOMBAY["LON"])])
    def test_response_types(self,LAT, LON):
        validate(instance=self.response.json(), schema=SCHEMA)

    def test_if_response_exists(self):



