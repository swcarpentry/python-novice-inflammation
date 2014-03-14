import requests
import cStringIO
import csv

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

def test_nonexistent_country():
    values = get_country_temperatures('XYZ')
    assert len(values) == 0, 'Should not have succeeded for country XYZ'

def test_canada():
    values = get_country_temperatures('CAN')
    assert len(values) > 0, 'Should have had data for country CAN'

def run_tests():
    test_nonexistent_country()
    test_canada()
    print 'all tests passed'

if __name__ == '__main__':
    run_tests()
