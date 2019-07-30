
from __future__ import print_function, unicode_literals
from datetime import date
from PyInquirer import prompt, print_json
from pprint import pprint
import json
import time
import datetime


questions = [
    {
        'type': 'input',
        'name': 'filepath',
        'message': 'Input filepath to message_1.json of the person you wish to count your messages with',
    }
]
answers = prompt(questions)
filepath = answers['filepath']

with open(filepath) as f:
    data = json.load(f)

count = 0
name = data['participants'][0]['name']
messages = data['messages']

for message in messages:
    count += 1

print("You and " + name + " sent each other " + str(count) + " messages.")

#Rawdata\messages\inbox\MikkelSA_F8NVPfJ-Vw\message_1.json
#Rawdata\messages\inbox\luciemartincova_1s6knlf85w\message_1.json
#Rawdata\messages\inbox\ErikEmilSteglich_KZD6nKJ_Gw\message_1.json
#Rawdata\messages\inbox\BajerGruppen_ussDUFrNeA\message_1.json
