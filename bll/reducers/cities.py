state = {
    'cities': {}
}


def reducer(action):
    match action['type']:
        case 'CREATE_CITY_ACTION':
            state['cities'][action['city']['name']] = action['city']

def create_city_action(city):
    reducer({'type': 'CREATE_CITY_ACTION', 'city': city})
