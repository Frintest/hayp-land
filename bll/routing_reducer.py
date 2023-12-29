from bll.cities_reducer import state as cities_state

state = {
    'path': '/',
    'command': ''
}


def reducer(action):
    match action['type']:
        case 'CHANGE_PATH_ACTION':
            if state['command'][6:] in cities_state['cities'] and state['command'][:6] == 'город ':
                state['path'] = f'/ город: {state["command"][6:]}'
            elif state['command'] == 'город *':
                state['path'] = '/'
            elif state['command'] == 'помощь':
                state['path'] = '/ помощь'
            elif state['command'] == 'рег ап':
                state['path'] = '/ рег ап'
                 
        case 'READ_COMMAND_ACTION':
            state['command'] = action['command']
    

def change_path_action():
    reducer({'type': 'CHANGE_PATH_ACTION'})


def read_command_action(command):
    reducer({'type': 'READ_COMMAND_ACTION', 'command': command})
