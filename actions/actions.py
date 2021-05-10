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
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
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
            try:
                response=requests.get("https://api.postalpincode.in/pincode/{}".format(pin))
                dta_pin=response.json()
           
                
                for i in dta_pin:
                    for j in i['PostOffice']:
                        state=j["State"]
            # Check if the responce is null then state = india
                try:
                    response=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
                    dta=response.json()
                except:
                    message="No respose found"
                    
                x=dta['data']
                y=x['regional']
                z=x["unofficial-summary"]
                
            #entities=tracker.latest_message['entities']
            #print(entities)
            #for e in entities:
               # if e['entity'] == 'state':
                   # state=e['value']
               
                value = state
                list_of_bool = [True for elem in y if value.title() in elem.values()]
                    # Value to be checked
                    
                    # check if bool list contains any True element i.e.
                    # if any dictionary contains the given value or not
             
                
                              
                if any(list_of_bool):
                    
                  
                    
                    for dicti in y:
                        if dicti['loc']==state.title():
                            print(dicti["loc"],dicti["confirmedCasesForeign"],dicti['confirmedCasesIndian'])
                            message= 'Showing Results for {} , confirmedCasesForeign:{} ,confirmedCasesIndian:{}'\
                            'discharged:{} ,totalConfirmed:{} , deaths: {} '\
                            .format(state,dicti["confirmedCasesForeign"],dicti['confirmedCasesIndian'],
                            dicti['discharged'],dicti["totalConfirmed"],dicti['deaths'])
                
                else:
                                
                    print(z[0]["active"],z[0]["deaths"])
                    message= 'No Results found for this state , Showing results for Total Summary'\
                    'active:{} ,deaths:{}'\
                    'recovered:{} ,source:{} , total: {} '\
                    .format(z[0]["active"],z[0]["deaths"],\
                    z[0]["recovered"],z[0]["source"],z[0]["total"])
                             
            except:
                
              
                try:
                    response=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
                    dta=response.json()
                except:
                    print("No data Found")
                    
                x=dta['data']
                y=x['regional']
                z=x["unofficial-summary"]
                
                
              
                message= 'No respose found for this pin showing results for Total Summary'\
                'active:{} ,deaths:{}'\
                'recovered:{} ,source:{} , total: {} '\
                .format(z[0]["active"],z[0]["deaths"],\
                z[0]["recovered"],z[0]["source"],z[0]["total"])
                
        if state:
            try:
                response=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
                dta=response.json()
            except:
                print("No data Found")
                
            x=dta['data']
            y=x['regional']
            z=x["unofficial-summary"]
            
            entities=tracker.latest_message['entities']
            print(entities)
            for e in entities:
                if e['entity'] == 'state':
                    state=e['value']
           
            value = state
            list_of_bool = [True for elem in y if value.title() in elem.values()]
                # Value to be checked
                
                # check if bool list contains any True element i.e.
                # if any dictionary contains the given value or not
            if any(list_of_bool):
                
                for dicti in y:
                    if dicti['loc']==state.title():
                        
                        #print(dicti["loc"],dicti["confirmedCasesForeign"],dicti['confirmedCasesIndian'])
                   
                        message= 'Showing Cases for {},confirmedCasesForeign:{} ,confirmedCasesIndian:{}'\
                        'discharged:{} ,totalConfirmed:{} , deaths: {} ,'.format(state,dicti["confirmedCasesForeign"]
                        ,dicti['confirmedCasesIndian'],dicti['discharged'],dicti["totalConfirmed"],dicti['deaths'])
            else:
            
                print(z[0]["active"],z[0]["deaths"])
                message= 'No State Found , Showing Values for Total Summary,active:{} ,deaths:{}'\
                'recovered:{} ,source:{} , total: {} '\
                .format(z[0]["active"],z[0]["deaths"],\
                z[0]["recovered"],z[0]["source"],z[0]["total"])
         
        dispatcher.utter_message(message)

        return []    
    
 
    
