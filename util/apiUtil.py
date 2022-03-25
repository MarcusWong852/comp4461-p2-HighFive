class ApiUtil():

    @staticmethod
    def getHKOUrl(dataType):
        return "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=" + dataType + "&lang=en"
