state = {
    'global': {}
}


def reducer(action):
    match action['type']:
        case 'ADD_GLOBAL_COMMAND':
            state['global'][action['desc']] = action['command']
            
def add_global_command(desc, command):
    reducer({'type': 'ADD_GLOBAL_COMMAND', 'desc': desc, 'command': command})
