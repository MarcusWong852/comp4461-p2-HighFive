import requests
from util.apiUtil import ApiUtil
from enum import Enum


class HKOApiDataType(Enum):
    LocalWeatherForecast = "flw"
    LocalWeatherReport = "rhrread"


class API():

    @staticmethod
    def fetchWeatherForecast():
        forecastData = {}

        try:
            forecastResponse = requests.get(
                ApiUtil.getHKOUrl(HKOApiDataType.LocalWeatherForecast))
            reportResponse = requests.get(
                ApiUtil.getHKOUrl(HKOApiDataType.LocalWeatherReport))

            if forecastResponse.status_code != 200 or reportResponse.status_code != 200:
                raise

            forecastData['forecastDesc'] = forecastResponse.json()[
                'forecastDesc']

            temperatureDataSet = reportResponse.json()['temperature']['data']
            for each in temperatureDataSet:
                if each['place'] == 'King\'s Park':
                    forecastData['temperature'] = each['value']

            return forecastData
        except Exception:
            print("Could not fetch temperature")
