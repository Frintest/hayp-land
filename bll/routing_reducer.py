from bll.cities_reducer import state as cities_state

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
            elif state['command'] == 'рег ап':
                state['path'] = '/ рег ап'
                 
        case 'READ_COMMAND_ACTION':
            state['command'] = action['command']
    

def changePathAction():
    reducer({'type': 'CHANGE_PATH_ACTION', 'cities': cities_state['cities']})


def readCommandAction(stdscr, command):
    reducer({'type': 'READ_COMMAND_ACTION', 'stdscr': stdscr, 'command': command})
