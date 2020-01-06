#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import boto3
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *


#CONFIGURATION_ENCODING_FORMAT = "utf-8"
#CONFIG_INI = "config.ini"
intents =["kaboe003:PatientIntent", "kaboe003:ZSTIntent", "kaboe003:MUIntent", "kaboe003:ZahnIntent", "kaboe003:Stop"]


class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


"""def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()
"""
def patient_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    patient_wrapper(hermes, intentMessage, conf)

def zst_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    zst_wrapper(hermes, intentMessage, conf)

def mu_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    mu_wrapper(hermes, intentMessage, conf)

def zahn_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    zahn_wrapper(hermes, intentMessage, conf)

def stop_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    stop_wrapper(hermes, intentMessage, conf)
    #data['piz'] = intentMessage.slots.slot1
    
def patient_wrapper(hermes, intentMessage, conf):
    print('Patient')
    hermes.publish_continue_session(intentMessage.session_id, "Herzlich Willkommen Patient 1", intents)
    hermes.publish_end_session(intentMessage.session_id, "Patient Beendet")

def mu_wrapper(hermes, intentMessage, conf):
    print('mu')
    hermes.publish_continue_session(intentMessage.session_id, "Bitte weiter", intents)
    #info['mu'] = intentMessage.slots.slot1

def zst_wrapper(hermes, intentMessage, conf):
    print('zst')
    hermes.publish_continue_session(intentMessage.session_id, "Bitte weiter", intents)
    #info['zst'] = intentMessage.slots.slot1

def zahn_wrapper(hermes, intentMessage, conf):
    print('zahn')
    hermes.publish_continue_session(intentMessage.session_id, "Bitte weiter", intents)
    #zaehne[str(intentMessage.slots.slot1) + str(intentMessage.slots.slot2)] = intentMessage.slots.slot3

def stop_wrapper(hermes, intentMessage, conf):
    print('Stop')
   
    
    
    
    
    

if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("kaboe003:PatientIntent", patient_intent_callback) \
        .subscribe_intent("kaboe003:ZSTIntent", zst_intent_callback)\
        .subscribe_intent("kaboe003:MUIntent", mu_intent_callback)\
        .subscribe_intent("kaboe003:ZahnIntent", zahn_intent_callback)\
        .subscribe_intent("kaboe003:Stop", stop_intent_callback)\
         .start()
