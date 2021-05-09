# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import requests
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_Hello_kiran"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Hello World Kiran avhd!")

        return []
 

    
    

   
    
    
class ActionSlotdemo(Action):
    def name(self) -> Text:
        return "action_slot_demo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name=tracker.get_slot("name")
        pins=tracker.get_slot("pin")
        leader_name=""
        if pins=="411048":
            leader_name="Kiran Avhad"
        else:
            leader_name="Narendra Modi"
        message="your name is {} and yr pin {} and Leaader{}".format(name,pins,leader_name)   
        
        dispatcher.utter_message(text=message)

        return []  
    
    
#class ActionRestarted(Action):
        


#    def name(self):
#        return "action_chat_restart"

#    def run(self, dispatcher, tracker, domain):
#        return [Restarted()]    
        
    
    
    
class Actionfindingcoronacases(Action):
    def name(self) -> Text:
              
        return "action_find_corona"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
       
        name=tracker.get_slot("name")
        pins=tracker.get_slot("pin")
        
        entities=tracker.latest_message['entities']
        
        print(entities)
        pin=None
        state=None
        for e in entities:
            if e['entity'] == 'pin':
                pin=e['value']
            elif e['entity'] =='state':
                state=e['value']
            print(pin)
            print(state)
        if pin:
            response=requests.get("https://api.postalpincode.in/pincode/{}".format(pin))
            dta_pin=response.json()
            for i in dta_pin:
                for j in i['PostOffice']:
                    state=j["State"]
        # Check if the responce is null then state = india
            response=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
            dta=response.json()
            x=dta['data']
            y=x['regional']
            z=x["unofficial-summary"]
            
        #entities=tracker.latest_message['entities']
        #print(entities)
        #for e in entities:
           # if e['entity'] == 'state':
               # state=e['value']
            for kk in y:
                if kk['loc']==state.title():
                    found=1
                    break
                else:
                    found=2
                    
            if found==1:
                          
                for dicti in y:
                    if dicti['loc']==state.title():
                        print(dicti["loc"],dicti["confirmedCasesForeign"],dicti['confirmedCasesIndian'])
                        message= 'confirmedCasesForeign:{} ,confirmedCasesIndian:{}'\
                        'discharged:{} ,totalConfirmed:{} , deaths: {} '\
                        .format(dicti["confirmedCasesForeign"],dicti['confirmedCasesIndian'],
                        dicti['discharged'],dicti["totalConfirmed"],dicti['deaths'])
            if found==2:
                print(z[0]["active"],z[0]["deaths"])
                message= 'active:{} ,deaths:{}'\
                'recovered:{} ,source:{} , total: {} '\
                .format(z[0]["active"],z[0]["deaths"],\
                z[0]["recovered"],z[0]["source"],z[0]["total"])
                         
                     
        if state:
            response=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
            dta=response.json()
            x=dta['data']
            y=x['regional']
           
            
            entities=tracker.latest_message['entities']
            print(entities)
            for e in entities:
                if e['entity'] == 'state':
                    state=e['value']
           
            for kk in y:
                
                if kk['loc']==state.title():
                    found=1
                    break
                else:
                    found=2  
                   
            if found==1:
                for dicti in y:
                    if dicti['loc']==state.title():
                        #print(dicti["loc"],dicti["confirmedCasesForeign"],dicti['confirmedCasesIndian'])
                   
                        message= 'confirmedCasesForeign:{} ,confirmedCasesIndian:{}'\
                        'discharged:{} ,totalConfirmed:{} , deaths: {} ,'.format(dicti["confirmedCasesForeign"]
                         ,dicti['confirmedCasesIndian'],dicti['discharged'],dicti["totalConfirmed"],dicti['deaths'])
            if found ==2:
                print(z[0]["active"],z[0]["deaths"])
                message= 'active:{} ,deaths:{}'\
                'recovered:{} ,source:{} , total: {} '\
                .format(z[0]["active"],z[0]["deaths"],\
                z[0]["recovered"],z[0]["source"],z[0]["total"])
         
        dispatcher.utter_message(message)

        return []    
    
 
    
