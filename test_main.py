from http import HTTPStatus
import requests
import pytest
from constants import Key, London, Amsterdam, Bombay, city_names, city_names_incorrect


# test using lat and lon

class TestApiCoords:

    def test_london(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={London['LAT']}&lon={London['LON']}&appid={Key}")
        assert response.status_code == HTTPStatus.OK

    def test_amsterdam(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={Amsterdam['LAT']}&lon={Amsterdam['LON']}&appid={Key}")
        assert response.status_code == HTTPStatus.OK

    def test_bombay(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={Bombay['LAT']}&lon={Bombay['LON']}&appid={Key}")
        assert response.status_code == HTTPStatus.OK


class TestApiCity:
    # test using city names

    @staticmethod
    @pytest.mark.parametrize("city_name,expected", [(city_names[0], HTTPStatus.OK), (city_names[1], HTTPStatus.OK),
                                                    (city_names[2], HTTPStatus.OK)])
    def test_city(city_name, expected):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
        assert response.status_code == expected

    @staticmethod
    @pytest.mark.parametrize("city_name,expected",
                             [(city_names_incorrect[0], HTTPStatus.OK), (city_names_incorrect[1], HTTPStatus.OK),
                              (city_names_incorrect[2], HTTPStatus.OK)])
    def test_city_incorrect(city_name, expected):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
        assert response.status_code == expected


class TestApiError:

    def test_coords_letter(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={'a'}&lon={'b'}&appid={Key}")
        assert response != HTTPStatus.OK

    def test_coords_number(self):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={'1'}&lon={'2'}&appid={Key}")
        assert response != HTTPStatus.OK

    def test_city_letter(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={'a'}&appid={Key}")
        assert response != HTTPStatus.OK

    def test_city_number(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={'1'}&appid={Key}")
        assert response != HTTPStatus.OK


class TestApiErrorParam:

    @staticmethod
    @pytest.mark.parametrize("lat,lon", [("a", "b"), ("1", "2")])
    def test_coords(lat, lon):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}")
        assert response != HTTPStatus.OK

    @staticmethod
    @pytest.mark.parametrize("city_name", ["a", "1"])
    def test_city(city_name):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
        assert response != HTTPStatus.OK

