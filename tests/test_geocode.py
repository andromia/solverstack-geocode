from . import common
from app import geocode


def test_geocode():
    zipcodes = common.TESTING_CSV_DF.zipcode\
        .str.zfill(5)\
        .tolist()
    countries = common.TESTING_CSV_DF.country\
        .str.lower()

    len(zipcodes) == len(geocode.geocode_zipcodes(zipcodes, countries))