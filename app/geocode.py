import pgeocode


def geocode_zipcodes(zipcodes: list, countries: list):
    """
    Use pgeocode to get latitude and longitude for zipcodes.

    :zipcodes:      list-like of clean zipcodes
    :countries:     list-like of expected country abbreviations

    :return:        list of lists containing [[lat, lon], ...]
    """
    geocodes = []

    for i, country in enumerate(countries):
        nomi = pgeocode.Nominatim(country)
        results = nomi.query_postal_code(zipcodes[i])

        geocodes.append([results.latitude, results.longitude])
    
    return geocodes

