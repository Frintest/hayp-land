from ui.utilities.color_pair import set_color_pair
from bll.reducers.help import add_global_command
from bll.state import state

def help_page():
    def print_command(desc, command):
        print(set_color_pair('RESET') + f'{desc:<27}', end='')
        print(set_color_pair('APP') + f'{command}')
    
    for desc, command in state['help']['global'].items():
        print_command(desc, command)
    