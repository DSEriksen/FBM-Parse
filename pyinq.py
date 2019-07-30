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


print(filepath)
