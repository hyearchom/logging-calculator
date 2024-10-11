#!/usr/bin/env python3
# the previous line is for unix systems and can be freely deleted
from datetime import datetime
import os

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(SCRIPT_PATH, 'settings')
# looking for necessary folder, or creating it
if not os.path.exists(SETTINGS_PATH): os.mkdir(SETTINGS_PATH)

HISTORY_PATH = os.path.join(SETTINGS_PATH, 'calculator.md')

def log_entry(content, show=True):
    """writes a line into history file"""
    with open(PATH_TO_FILE, 'a+') as file:
        file.write(f'{content}\n')
    if show:
        print(content)

try:
    while True:
        calculation = input('Insert calculation:\n')
        result = eval(calculation)
        time = datetime.now().strftime('%Y-%m-%d %A %H:%M')

        log_entry(f'{calculation}={result}')
        log_entry(time, False)
        log_entry('')

    """ User can end aplication by inserting blank
    or by pressing Ctrl+C"""    
except (SyntaxError, KeyboardInterrupt):
    print('Aplication terminated')