"""
Here are the constants used by test_main.py and helpers.py
This file also includes the key used for api testing
"""

KEY = "59e62469a3da06b2a9a30ff73c2c0d05"

# london coordinates
LONDON = {
    "COUNTRY": "England",
    "LAT": 51.5073219,
    "LON": -0.1276474
}

# AMSTERDAM coordinates
AMSTERDAM = {
    "COUNTRY": "Netherlands",
    "LAT": 52,
    "LON": 4
}

# BOMBAY coordinates
BOMBAY = {
    "COUNTRY": "India",
    "LAT": 19,
    "LON": 72.48
}
CITY_NAMES = "Tokyo", "Delhi", "Dhaka", "New York", "Moscow", "Paris"
CITY_NAMES_DIFFERENT_CASES = "tOkYo", "DeLhi", "dhaKa", "new york", "MoCscOw", "PaRiS"

# Json testing
TEST_RESPONSE = {
    "base": "stations",
    "clouds": {
        "all": 100
    },
    "cod": 200,
    "coord": {
        "lon": 139,
        "lat": 35
    },
    "dt": 1652173547,
    "id": 1851632,
    "main": {
        "temp": 288.29,
        "feels_like": 287.66,
        "temp_min": 288.29,
        "temp_max": 288.29,
        "pressure": 1020,
        "humidity": 69,
        "sea_level": 1020,
        "grnd_level": 991
    },
    "name": "Shuzenji",
    "sys": {
        "country": "JP",
        "sunrise": 1652125502,
        "sunset": 1652175351
    },
    "timezone": 32400,
    "visibility": 10000,
    "weather": [
        {
            "id": 804,
            "main": "Clouds",
            "description": "overcast clouds",
            "icon": "04d"
        }
    ],
    "wind": {
        "speed": 1.92,
        "deg": 84,
        "gust": 2.91
    }
}  # response from open weather api for testing purposes
SCHEMA = {
    "type": "object",
    "properties": {

        "base": {
            "type": "string"
        },

        "clouds": {
            "type": "object",
            "properties": {

                "all": {
                    "type": "number"
                }
            }
        },

        "cod": {
            "type": "number"
        },

        "coord": {
            "type": "object",
            "properties": {
                "lon": {"type": "number"},
                "lat": {"type": "number"}
            }
        },

        "dt": {"type": "number"},

        "id": {"type": "number"},

        "main": {
            "type": "object",
            "properties": {
                "temp": {"type": "number"},
                "feels_like": {"type": "number"},
                "temp_min": {"type": "number"},
                "temp_max": {"type": "number"},
                "pressure": {"type": "number"},
                "humidity": {"type": "number"},
                "sea_level": {"type": "number"},
                "grnd_level": {"type": "number"}
            }
        },

        "name": {"type": "string"},

        "sys": {
            "type": "object",
            "properties": {
                "country": {"type": "string"},
                "sunrise": {"type": "number"},
                "sunset": {"type": "number"}
            }
        },

        "timezone": {"type": "number"},

        "visibility": {"type": "number"},

        "weather": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "main": {"type": "string"},
                    "description": {"type": "string"},
                    "icon": {"type": "string"}
                }
            }
        },
        "wind": {
            "type": "object",
            "properties": {
                "speed": {"type": "number"},
                "deg": {"type": "number"},
                "gust": {"type": "number"}
            }
        }

    }
}  # My Schema full of frustration - it works :D
