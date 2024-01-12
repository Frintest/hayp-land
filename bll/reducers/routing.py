from bll.reducers.cities import state as cities_state


state = {
    'path': '/',
    'command': '',
    'path_prefix': '/ '
}


def reducer(action: dict):
    match action['type']:
        case 'CHANGE_PATH_ACTION':
            path_prefix = state['path_prefix']
            def update_path(command: str):
                state['path'] = f'{path_prefix}{command}'
            
            
            city = state['command'][len('город '):]
            city_command = state['command'][:len('город ')]
            if city_command == 'город ' and city in cities_state['cities']:
                update_path(f'город: {city}')
                
            elif state['command'] == 'город *':
                state['path'] = '/'
                
            elif state['command'] == 'помощь':
                update_path('помощь')
                
            elif state['command'] == 'рег ап':
                update_path('рег ап')
                 
                 
        case 'READ_COMMAND_ACTION':
            state['command'] = action['command']
    

def change_path_action():
    reducer({'type': 'CHANGE_PATH_ACTION'})


def read_command_action(command: str):
    reducer({'type': 'READ_COMMAND_ACTION', 'command': command})
