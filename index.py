import os
from routing.index import routing
from bll.reducers.routing import change_path_action, read_command_action
from ui.common.command import read_command
from storage.cities import create_cities
from storage.users import create_users
from storage.patent import create_patents
from storage.help import create_help_commands


create_help_commands()
create_cities()
create_users()
create_patents()

def render():
    while True:
        os.system("cls")
        routing()
        read_command_action(read_command())
        change_path_action()


render()
