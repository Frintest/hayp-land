state = {
    'global': {}
}


def reducer(action: dict):
    match action['type']:
        case 'ADD_GLOBAL_COMMAND':
            state['global'][action['desc']] = action['command']


def add_global_command(desc: str, command: str):
    reducer({'type': 'ADD_GLOBAL_COMMAND', 'desc': desc, 'command': command})
