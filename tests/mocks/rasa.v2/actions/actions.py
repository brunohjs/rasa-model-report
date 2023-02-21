# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"
from typing import Any
from typing import Dict
from typing import List
from typing import Text

from rasa_sdk import Action
from rasa_sdk import ActionExecuted
from rasa_sdk import FollowupAction
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_message(response = "utter_test")
        return [
            FollowupAction("action_test"),
            FollowupAction("action_test"),
            ActionExecuted("action_test2"),
            FollowupAction( "action_test3" ),
            FollowupAction("validate_slot")
        ]
