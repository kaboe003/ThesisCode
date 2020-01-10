#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import dynamo
piz = None;


intents = ["kaboe003:PatientIntent", "kaboe003:ZSTIntent", "kaboe003:MUIntent", "kaboe003:ZahnIntent"]


def patient_intent_callback(hermes, intentMessage):
    patient_wrapper(hermes, intentMessage)
    hermes.publish_continue_session( intentMessage.session_id, "Herzlich Willkommen zu Ihrer Untersuchung Patient {}".format(piz),intents)
    
def patient_wrapper(hermes, intentMessage):
    print('Patient')
    piz = intentMessage.slots.id.first().value
    piz = int(piz)
    dynamo.set_value("data", "piz", piz)
    
def zst_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    zst_wrapper(hermes, intentMessage)
    hermes.publish_continue_session(intentMessage.session_id, "Verstanden", intents)
    
def zst_wrapper(hermes, intentMessage):
    print('zst')
    value = intentMessage.slots.ZSTStatus.first().value
    if value in ("Ne", "Kein", "nicht vorhanden", "Nein"):
        dynamo.set_value("info", "zst", "Nein")
    if value in ("Jo", "Vorhanden", "Ja"):
        dynamo.set_value("info", "zst", "Ja")
    

def mu_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    mu_wrapper(hermes, intentMessage)
    hermes.publish_continue_session(intentMessage.session_id, "Verstanden", intents)

def mu_wrapper(hermes, intentMessage):
    print('mu')
    value = intentMessage.slots.MUStatus.first().value
    if value in ("Ne", "Kein", "nicht vorhanden"):
        dynamo.set_value("info", "mu", "Nein")
    if value in ("Jo", "Vorhanden"):
        dynamo.set_value("info", "mu", "Ja")

def zahn_intent_callback(hermes, intentMessage):
    zahn_wrapper(hermes, intentMessage)
    hermes.publish_continue_session(intentMessage.session_id, "Verstanden", intents)
    
def zahn_wrapper(hermes, intentMessage):
    try:
        if len(dynamo.zaehne) <= 32:
            print('zahn')
            quadrant = int(intentMessage.slots.quadrant.first().value)
            zahn = int(intentMessage.slots.zahl.first().value)
            value = intentMessage.slots.status.first().value
            dynamo.set_value("zaehne", str(quadrant) + str(zahn), value)
    except (AttributeError):
        print("Bitte erneut eingeben")
       

def stop_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    stop_wrapper(hermes, intentMessage)
    # data['piz'] = intentMessage.slots.slot1
    hermes.publish_end_session(intentMessage.session_id, "Vielen Dank und auf Wiedersehen")
   
        

def stop_wrapper(hermes, intentMessage):
    if "zst" not in dynamo.info:
        hermes.publish_continue_session(intentMessage.session_id, "Bitte Zahnstein angeben", intents)
    elif "mu" not in dynamo.info:
        hermes.publish_continue_session(intentMessage.session_id, "Bitte Zahnstein angeben", intents)
    elif "piz" not in dynamo.data:
        hermes.publish_continue_session(intentMessage.session_id, "Bitte Zahnstein angeben", intents)
    else:
        #dynamo.new_entry()
        stop_wrapper(hermes, intentMessage)


def session_started(hermes, session_started_message):
    print("Session started")
    hermes.publish_start_session_action(None, "Herzlich Willkommen zu Ihrer Untersuchung", intents, True, False, None)
    
def session_ended(hermes, session_ended_message):
    print("Session ended")
    








    

def stop_wrapper(hermes, intentMessage):
    print('Stop')
    hremes.publish_end_session(intentMessage.session_id, "Vielen Dank")
   # dynamo new_entry()

if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("kaboe003:PatientIntent", patient_intent_callback) \
        .subscribe_intent("kaboe003:ZSTIntent", zst_intent_callback) \
        .subscribe_intent("kaboe003:MUIntent", mu_intent_callback) \
        .subscribe_intent("kaboe003:ZahnIntent", zahn_intent_callback) \
        .subscribe_intent("kaboe003:Stop", stop_intent_callback)\
        .subscribe_session_started(session_started)\
        .subscribe_session_ended(session_ended)\
        .loop_forever()
       
        
            
