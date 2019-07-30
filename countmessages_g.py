
from __future__ import print_function, unicode_literals
from datetime import date
from PyInquirer import prompt, print_json
from pprint import pprint
import json
import time
import datetime
import tablib


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

# Vars
participants = data['participants']
messages = data['messages']

# Scanning for names
names = []
nameCount = 0
for entry in participants:
    nameCount += 1
    names.append(entry['name'])


# Scanning for messages
totalCount = 0
for message in messages:
    totalCount += 1

# Scannning for messages per person
    # Load all participants names and msgcount
person = {}
person_dict = []
messageStats = {}
stats = []
activeCount = 0

for i in range(len(names)):
    person['name'] = names[i]
    person['msgcount'] = 0
    person_dict.append(person.copy())

    # Scan for name match and add to counter
person_msgCount = 0
for i in range(len(names)):
    person_msgCount = 0
    for j in range(len(messages)):
        if names[i] == messages[j]['sender_name']:
            person_msgCount += 1
            activeCount += 1
    person_dict[i]['msgcount'] = person_msgCount

# print(person_dict)

# Load all into stats[]
messageStats['totalCount'] = totalCount
messageStats['activeCount'] = activeCount

stats.append(person_dict.copy())
stats.append(messageStats.copy())

with open('exportdata.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=4)

headers = ('Name', 'Message Count')
statsXLS = tablib.Dataset()
for i in range(len(names)):
    statsXLS.append((
        str(person_dict[i]['name']), person_dict[i]['msgcount']
    ))

open('statsXLS.xls', 'wb').write(statsXLS.xls)

#First message sent Epoch time 1420468791315
timestamp = 1420468791315/1000.0
data_first_msg = datetime.datetime.fromtimestamp(timestamp)
print(data_first_msg)

print("Dumped information into exportdata.json")

# Rawdata\messages\inbox\BajerGruppen_ussDUFrNeA\message_1.json
