from bll.reducers.cities import create_city_action


def create_cities():
    create_city_action(
        { 
            'name': 'АтлантCity',
            'display_color': 'CYAN',
            'users': {
                'frunkers': {},
                'кирилл': {},
            },
            'structures': {
                'Федеральное экономическое хранилище (ФЭХ)': {},
            },
        },
    )
