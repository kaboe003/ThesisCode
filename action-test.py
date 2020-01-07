#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import configparser
import boto3
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import dynamo


intents = ["kaboe003:PatientIntent", "kaboe003:ZSTIntent", "kaboe003:MUIntent", "kaboe003:ZahnIntent"]


def patient_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    patient_wrapper(hermes, intentMessage)


def zst_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    zst_wrapper(hermes, intentMessage)


def mu_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    mu_wrapper(hermes, intentMessage)


def zahn_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    zahn_wrapper(hermes, intentMessage)


def stop_intent_callback(hermes, intentMessage):
    #conf = read_configuration_file(CONFIG_INI)
    stop_wrapper(hermes, intentMessage)
    # data['piz'] = intentMessage.slots.slot1
    
def session_started(hermes, session_started_message):
    print("Session started")
    
   

    
def patient_wrapper(hermes, intentMessage):
    print(intentMessage.session_id)
    print('Patient')
    piz = int(intentMessage.slots.id.first().value)
    hermes.publish_continue_session(intentMessage.session_id, "Herzlich Willkommen zu Ihrer Untersuchung Patient {}".format(piz)  , intents)
    dynamo.set_value("data", "piz", piz)
    
    


def mu_wrapper(hermes, intentMessage):
    print('mu')
    value = intentMessage.slots.MUStatus.first().value
    hermes.publish_continue_session(intentMessage.session_id, "Verstanden", intents)
    dynamo.set_value("info", "mu", value)


def zst_wrapper(hermes, intentMessage):
    print('zst')
    value = intentMessage.slots.ZSTStatus.first().value
    hermes.publish_continue_session(intentMessage.session_id, "Verstanden", intents)
    dynamo.set_value("info", "zst", value)


def zahn_wrapper(hermes, intentMessage):
    print('zahn')
    quadrant = int(intentMessage.slots.quadrant.first().value)
    zahn = int(intentMessage.slots.zahl.first().value)
    value = intentMessage.slots.status.first().value
    hermes.publish_continue_session(intentMessage.session_id, "Verstanden", intents)
    dynamo.set_value("zaehne", str(quadrant) + str(zahn), value)
    dynamo.printAll()


def stop_wrapper(hermes, intentMessage):
    print('Stop')
    hremes.publish_end_session(intentMessage.session_id, "Vielen Dank")
    dynamo.printAll()

if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("kaboe003:PatientIntent", patient_intent_callback) \
        .subscribe_intent("kaboe003:ZSTIntent", zst_intent_callback) \
        .subscribe_intent("kaboe003:MUIntent", mu_intent_callback) \
        .subscribe_intent("kaboe003:ZahnIntent", zahn_intent_callback) \
        .subscribe_intent("kaboe003:Stop", stop_intent_callback)\
        .subscribe_session_started(session_started)\
        .loop_forever()
       
        
            
