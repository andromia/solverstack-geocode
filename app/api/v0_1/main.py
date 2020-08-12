from json import loads
from typing import List
from numpy import zeros

from flask import jsonify, make_response, request

from app import geocode

from . import bp


@bp.route("/geocode", methods=["POST"])
def geocode_procedure():
    """
    Main RPC endpoint for passing input data for geocoded outputs.

    :zipcode:      str of 5-digit padded zipcodes 
    :country:      str of country abbreviations

    :return:       list of dicts 
    [
        {
            "zipcode": str, 
            "country": str, 
            "latitude": float, 
            "longitude": float
        } ...
    ]              
    """
    body = loads(request.data)

    zipcodes = zeros(len(body))
    countries = zeros(len(body))

    for i, row in enumerate(body):
        zipcodes[i] = row["zipcode"].strip()[:5].zfill(5)
        countries[i] = row["country"].strip().lower()

    geocodes = geocode.geocode_zipcodes(zipcodes, countries)

    response = [
        {
            "zipcode": body[i]["zipcode"],
            "country": body[i]["country"],
            "latitude": geo[0],
            "longitude": geo[1],
        }
        for i, geo in enumerate(geocodes)
    ]

    return jsonify(response)
