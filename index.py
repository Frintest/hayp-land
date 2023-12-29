import os
from routing.index import routing
from bll.routing_reducer import change_path_action, read_command_action
from bll.cities_reducer import create_city_action
from ui.common.command import read_command

create_city_action(
    {
        'name': 'АтлантCity',
        'display_color': 'CYAN',
        'players': {
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
