import datetime
from typing import Any, Text, Dict, List
from api.api import API
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionWeatherForecast(Action):

    def name(self) -> Text:
        return "action_weather_forecast"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        weatherForecast = API.fetchWeatherForecast()
        temperature = API.fetchTemperature()
        dispatcher.utter_message(
            text=f"The temperature now is {temperature}C, {weatherForecast}")
        return []

class GreetTimeofDay(Action):

    def name(self) -> Text:
        return "action_greet_timeofday"

    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            dt=datetime.datetime.now()
            if dt.hour < 12:
                dispatcher.utter_message(text=f"Good Morning!")
            else:
                dispatcher.utter_message(text=f"Good Evening!")

            return []

class TimeofDay(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            dt=datetime.datetime.now()
            fullmonth=dt.strftime("%B")
            fullweekday=dt.strftime("%A")
            dispatcher.utter_message(text=f"Today is {fullweekday} {dt.day}th of {fullmonth}, {dt.hour}:{dt.minute}.")

            return []