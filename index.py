import os
from routing.index import routing
from bll.reducers.routing import change_path_action, read_command_action
from bll.reducers.cities import create_city_action
from ui.common.command import read_command

create_city_action(
    {
        'name': 'АтлантCity',
        'display_color': 'CYAN',
        'users': {
            'frunkers': {},
            'кирилл': {}
        },
        'structures': {'Федеральное экономическое хранилище (ФЭХ)': {}}
    }
)


def render():
    while True:
        os.system("cls")
        routing()
        read_command_action(read_command())
        change_path_action()

render()
