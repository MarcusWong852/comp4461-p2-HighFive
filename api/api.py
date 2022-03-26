import requests
from util.apiUtil import ApiUtil
from enum import Enum


class HKOApiDataType(Enum):
    LocalWeatherForecast = "flw"
    LocalWeatherReport = "rhrread"


class API():

    @staticmethod
    def fetchWeatherForecast():
        try:
            response = requests.get(
                ApiUtil.getHKOUrl(HKOApiDataType.LocalWeatherForecast.value))

            if response.status_code != 200:
                raise

            return response.json()[
                'forecastDesc']
        except Exception:
            print("Could not fetch weather forecast")

    @staticmethod
    def fetchTemperature():
        try:
            response = requests.get(
                ApiUtil.getHKOUrl(HKOApiDataType.LocalWeatherReport.value))

            if response.status_code != 200:
                raise

            temperatureDataSet = response.json()['temperature']['data']
            for each in temperatureDataSet:
                if each['place'] == 'King\'s Park':
                    return each['value']
        except Exception:
            print("Could not fetch weather temperature")
