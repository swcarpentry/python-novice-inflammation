import requests
import cStringIO
import csv

def compare_countries(left_country, right_country):
    '''
    Compare average surface temperatures for two countries over time.
    '''
    left_data = get_country_temperatures(left_country)
    right_data = get_country_temperatures(right_country)
    result = []
    for ( (left_year, left_value), (right_year, right_value) ) in zip(left_country, right_country):
        assert left_year == right_year, 'Year mismatch: {0} vs {1}'.format(left_year, right_year)
        result.append([left_year, left_value - right_value])
    return result

def get_country_temperatures(country):
    '''
    Get average surface temperature by country from the World Bank.
    Result is [ [year, value], [year, value], ...].
    '''

    base_url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/{0}.csv'
    actual_url = base_url.format(country)
    response = requests.get(actual_url)
    reader = cStringIO.StringIO(response.text)
    wrapper = csv.reader(reader)
    result = []
    for record in wrapper:
        if record[0] != 'year':
            year = int(record[0])
            value = float(record[1])
            result.append([year, value])
    return result
