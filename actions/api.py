import requests
import json

class API():

    @staticmethod
    def fetchTemperature():
        url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise

            temperatureDataSet = response.json()['temperature']['data']
            for each in temperatureDataSet:
                if each['place'] == 'King\'s Park':
                    return each['value']
        except Exception:
            print("Could not fetch temperature")