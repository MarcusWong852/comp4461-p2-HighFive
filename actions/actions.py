from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import api


class ActionWeatherForecast(Action):

    def name(self) -> Text:
        return "action_weather_forecast"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        weatherForecast = api.fetechWeatherForecast()
        temperature = api.fetchTemperature()
        dispatcher.utter_message(
            text=f"The temperature is {temperature}C, {weatherForecast}")
        return []
