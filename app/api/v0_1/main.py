from . import bp
from app import geocode

from json import loads
from typing import List

from flask import jsonify, make_response, request
import requests


CRUD_URL: str = "http://localhost:5006/api/v0.1/geocode"


@bp.route("/geocode", methods=["POST"])
def geocode_procedure():
    """
    Main RPC endpoint for passing input data for geocoded outputs.

    :zipcode:      str of 5-digit padded zipcodes 
    :country:      str of country abbreviations
    """
    body: dict = loads(request.data)
    stack_id: int = body["stack_id"]

    zipcodes: list = [None] * len(body["zipcodes"])
    countries: list = [None] * len(body["zipcodes"])

    for i, row in enumerate(body["zipcodes"]):
        zipcodes[i]: str = row["zipcode"].strip()[:5].zfill(5)
        countries[i]: str = row["country"].strip().lower()

    geocodes: list = geocode.geocode_zipcodes(zipcodes, countries)

    results = {
        "stack_id": stack_id,
        "geocodes": [
            {
                "zipcode": zipcodes[i],
                "country": countries[i],
                "latitude": geo[0],
                "longitude": geo[1],
            }
            for i, geo in enumerate(geocodes)
        ],
    }

    try:
        response = requests.post(CRUD_URL, headers=request.headers, json=results,)

        return make_response(jsonify(loads(response.text)), 200)

    except:

        return make_response(jsonify(results), 200)
