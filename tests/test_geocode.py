from . import common
from app import geocode

import logging
import json
from typing import List
from pandas import DataFrame


def test_main_procedure(client, auth_header: dict, data: List[dict]):
    input_data: dict = {"stack_id": 1, "zipcodes": data}
    logging.debug(f"input data : {input_data}")
    logging.debug(f"endpoint: {common.ENDPOINT}")

    response = client.post(common.ENDPOINT, headers=auth_header, json=input_data)
    output: dict = json.loads(response.get_data())

    assert len(output["geocodes"]) == len(data)


def test_main_procedure_invalid(client, auth_header: dict):
    data = [
        {"zipcode": "07981", "country": "US"},
        {"zipcode": "07981", "country": "US"},
        {"zipcode": "07981", "country": "CA"},
        {"zipcode": "07981", "country": "US"},
    ]

    input_data: dict = {"stack_id": 1, "zipcodes": data}
    logging.debug(f"input data : {input_data}")
    logging.debug(f"endpoint: {common.ENDPOINT}")

    response = client.post(common.ENDPOINT, headers=auth_header, json=input_data)
    output: dict = json.loads(response.get_data())

    assert len(output["geocodes"]) == len(data)


def test_geocode(df: DataFrame):
    zipcodes: List[str] = df.zipcode.str.zfill(5).tolist()
    countries: List[str] = df.country.str.lower()

    len(zipcodes) == len(geocode.geocode_zipcodes(zipcodes, countries))
