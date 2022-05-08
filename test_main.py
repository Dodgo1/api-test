import requests
import pytest
from http import HTTPStatus
from constants import Key,London,Amsterdam,Bombay,city_names,city_names_incorrect

#test using lat and lon

def test_status():
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={London['LAT']}&lon={London['LON']}&appid={Key}")
    assert response.status_code == HTTPStatus.OK

def test_status():
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={Amsterdam['LAT']}&lon={Amsterdam['LON']}&appid={Key}")
    assert response.status_code == HTTPStatus.OK


def test_status():
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={Bombay['LAT']}&lon={Bombay['LON']}&appid={Key}")
    assert response.status_code == HTTPStatus.OK

# test using city names

@pytest.mark.parametrize("city_names,expected", [(city_names[0],HTTPStatus.OK),(city_names[1],HTTPStatus.OK),(city_names[2],HTTPStatus.OK)])
def test_city(city_names,expected):
    response = response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_names}&appid={Key}")
    assert response.status_code == expected

@pytest.mark.parametrize("city_name,expected", [(city_names_incorrect[0],HTTPStatus.OK),(city_names_incorrect[1],HTTPStatus.OK),(city_names_incorrect[2],HTTPStatus.OK)])
def test_city_incorrect(city_name,expected):
    response = response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Key}")
    assert response.status_code == expected
