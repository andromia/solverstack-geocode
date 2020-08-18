from . import common
from app import geocode, create_app
from app import __version__

from config import Config

from . import common

import logging
import pytest
import json



class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


@pytest.fixture
def client():
    yield create_app(TestConfig).test_client()


def test_main_procedure(client):
    input_data = common.DATA
    logging.debug(f"input data : {input_data}")

    endpoint = f"/api/{__version__}/geocode"
    logging.debug(f"endpoint: {endpoint}")

    response = client.post(endpoint, json=input_data)
    output = json.loads(response.get_data())

    assert len(output) == len(common.DATA)


def test_geocode():
    zipcodes = common.TESTING_CSV_DF.zipcode\
        .str.zfill(5)\
        .tolist()
    countries = common.TESTING_CSV_DF.country\
        .str.lower()

    len(zipcodes) == len(geocode.geocode_zipcodes(zipcodes, countries))