
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
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


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
        
        message = "'" + quote + "'"## " - [" + author + "]" ##(" + permalink + ")"
        dispatcher.utter_message(message) 
        return []

class ActionSetQuarantineDate(Action):
    def name(self) -> Text:
        return "action_start_quarantine"

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message['text']
        dt=datetime.datetime.now()
        fullmonth=dt.strftime("%B")
        fullweekday=dt.strftime("%A")
        dictionary={}
        dictionary['date'] = dt.day
        dictionary['month'] = dt.month
        dictionary['year'] = dt.year
        with open("output.json", "w") as outfile:
            json.dump(dictionary, outfile)
        dispatcher.utter_message(text=f"Your quarantine starts now, today is {fullweekday} {dt.day}th of {fullmonth}") 
        ##dispatcher.utter_message(text=f"{text}") 
        return []

class ActionCanleave(Action):
    def name(self) -> Text:
        return "action_question_can_leave"

    def run(self, dispatcher, tracker, domain):
        dt=datetime.datetime.now()
        with open('output.json') as json_file:
            data = json.load(json_file)
        startdate = datetime.datetime(data['year'], data['month'], data['date'])
        enddate = datetime.datetime(dt.year, dt.month, dt.day)
        difference = enddate - startdate
        if difference.days > 14:
            dispatcher.utter_message(text=f"You made it! Hope we don't meet again 🤣.")
        elif difference.days <= 14:
            dispatcher.utter_message(text=f"Add oil!")
            percentage_left=(14-difference.days)/14*100
            dispatcher.utter_message(text=f"You still have {percentage_left}%, {difference.days}days to go ✨")
        return []

# class ActionminiWordle(Action):
#     def name(self) -> Text:
#         return "action_play_mini_wordle"

#     def run(self, dispatcher, tracker, domain):
#         word_list={}
#         word_list['1'] = "SHIRT"
#         word_list['2'] = "HKUST"
#         word_list['3'] = "RALLY"
#         Selected_word={}
#         Selected_word1 = random.choice(list(word_list.values()))
#         dispatcher.utter_message(text=f"{Selected_word1}") 
#         Selected_word['1']= Selected_word1

#         with open("Selected.json", "w") as outfile:
#             json.dump(Selected_word, outfile)
#         dispatcher.utter_message(text=f"How about a Mini-Wordle? Let's start now!") 
#         ##dispatcher.utter_message(text=f"{text}") 
#         return [SlotSet("wordle_guess", Selected_word1)]

# class ActionPlayingminiwordle(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_wordle_answer"

#     def validate_wordle_guess(self, slot_value: Any, dispatcher, tracker, domain):
#         with open('Selected.json') as json_file:
#             data = json.load(json_file)
#         if slot_value.upper() != data['1']:
#             dispatcher.utter_message(text=f"Not this word")
#             return {"wordle_guess":None}
#         dispatcher.utter_message(text=f"Right Word") 
#         return {"wordle_guess": slot_value}
# class verifyanswer(Action):

#     def name(self) -> Text:
#         return "action_verify_answer"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         useranswer = tracker.latest_message['text']
#         answer = tracker.get_slot("wordle_guess")
#         if answer == useranswer:
#             dispatcher.utter_message(text="Right!")
#         else:
#             dispatcher.utter_message(text=f"Wrong!!")
#         return []