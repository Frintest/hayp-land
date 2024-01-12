state = {
    'cities': {}
}


def reducer(action: dict):
    match action['type']:
        case 'CREATE_CITY_ACTION':
            state['cities'][action['city']['name']] = action['city']


def create_city_action(city: str):
    reducer({'type': 'CREATE_CITY_ACTION', 'city': city})
