# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.api import Weather
from rasa_sdk.events import SlotSet
from actions.api import wikipid
from actions.api import get_news
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.latest_message['text']
        temp = Weather(city)['temp']

        dispatcher.utter_message(text="Hello from Crinmatic")
        dispatcher.utter_template("utter_temp", tracker, temp=temp)

        return []

class Actionwikipedia(Action):
    def name(self) -> Text:
        return "action_wikipedia_api"
    async def run(self, dispatcher: CollectingDispatcher, 
                              tracker : Tracker , 
                              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        wiki = tracker.get_slot("wiki")
        extract_data = wikipid(wiki)

        dispatcher.utter_message(template = "Hello from Crinmatic")
        return[]

class ActionGetNews(Action):
    def name(self) -> Text:
        return "action_get_news"
    async def run(self, dispatcher: CollectingDispatcher,
                                    tracker : Tracker,
                                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        country = tracker.get_slot("country")
        extract_news = get_news(country)
        
        dispatcher.utter_message(template = "Hello from Crinmatic")
        return []
        


