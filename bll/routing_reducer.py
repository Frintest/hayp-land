from bll.cities_reducer import state as cities_state
from ui.utilities.color_pair import setColorPair

CHANGE_PATH_ACTION = 'CHANGE_PATH_ACTION'
READ_COMMAND_ACTION = 'READ_COMMAND_ACTION'

state = {
    'path': '/',
    'command': ''
}


def reducer(action):
    match action['type']:
        case 'CHANGE_PATH_ACTION':
            if state['command'][6:] in action['cities'] and state['command'][:6] == 'город ':
                state['path'] = f'/ город: {state["command"][6:]}'
            elif state['command'] == 'город *':
                state['path'] = '/'
            elif state['command'] == 'помощь':
                state['path'] = '/ помощь'
        
        case 'READ_COMMAND_ACTION':
            stdscr = action['stdscr']
            stdscr.addstr(f'\nДля отображения списка команд введите: помощь\n')
            stdscr.addstr(f'{state["path"]}\n', setColorPair('RED'))
            stdscr.addstr(':]', setColorPair('*WHITE_ON_RED'))
            stdscr.addstr(' ')
            state['command'] = stdscr.getstr().decode('utf-8')
    

def changePathAction():
    reducer({'type': CHANGE_PATH_ACTION, 'cities': cities_state['cities']})


def readCommandAction(stdscr):
    reducer({'type': READ_COMMAND_ACTION, 'stdscr': stdscr})
