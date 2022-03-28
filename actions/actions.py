import datetime

import typing
import logging
import requests
import json
import re
import csv
import random

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
            elif dt.hour >= 12 and dt.hour <5:
                dispatcher.utter_message(text=f"Good Afternoon!")
            else:
                dispatcher.utter_message(text=f"Good Evening!")

            return []

class ReturnDate(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            dt=datetime.datetime.now()
            fullmonth=dt.strftime("%B")
            fullweekday=dt.strftime("%A")
            dispatcher.utter_message(text=f"Today is {fullweekday} {dt.day}th of {fullmonth}, the time now is {dt.hour}:{dt.minute}.")

            return []

class ActionGeek(Action):
    def name(self) -> Text:
        return "action_geek"

    def run(self, dispatcher, tracker, domain):
        request = json.loads(
            requests.get("http://quotes.stormconsultancy.co.uk/random.json").text
        )  
        author = request["author"]
        quote = request["quote"]
        ##permalink = request["permalink"]
        
        message = "'" + quote + "'" + " - [" + author + "]" ##(" + permalink + ")"
        dispatcher.utter_message(message) 
        return []