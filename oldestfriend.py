from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint

import json
import time
import datetime
from datetime import date

questions = [
    {
        'type': 'input',
        'name': 'filepath',
        'message': 'Input filepath to friends.json',
    }
]
answers = prompt(questions)
filepath = answers['filepath']

with open(filepath) as f:
    data = json.load(f)

#print(json.dumps(data,indent = 4, sort_keys=True))

data_len = len(data['friends'])
data_last = data['friends'][data_len-1]
data_last_name = data_last['name']
data_last_time = datetime.datetime.fromtimestamp(data_last['timestamp'])
today = date.today()
years = today.year - data_last_time.year

print("Your oldest friend is: " + str(data_last_name.replace("Ã¸", "ø")))
print("You have been friends since " +
      str(data_last_time.date())+" - "+str(years)+" years.")
