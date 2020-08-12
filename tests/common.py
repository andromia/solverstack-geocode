import logging
import os

from pandas import read_csv


TEST_ROOT = os.path.dirname(os.path.abspath(__file__))
CSV_TESTING_FILENAME = "zipcode_testing_data.csv"
CSV_TESTING_FILEPATH = os.path.join(TEST_ROOT, CSV_TESTING_FILENAME)


def get_csv():
    types = {"zipcode": str, "country": str}
    df = read_csv(CSV_TESTING_FILEPATH, dtype=types)
    logging.debug(f"filepath: {CSV_TESTING_FILEPATH} size: {df.shape}")

    return df

TESTING_CSV_DF = get_csv()