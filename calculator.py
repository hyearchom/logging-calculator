from datetime import datetime

PATH_TO_FILE = 'calculator.md'

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