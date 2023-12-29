from ui.utilities.color_pair import set_color_pair
from bll.help_reducer import add_global_command
from bll.state import state

def help_page():
    def print_command(desc, command):
        print(set_color_pair('RESET') + f'{desc:<27}', end='')
        print(set_color_pair('APP') + f'{command}')
    
    add_global_command('Отобразить все города', 'город *')
    add_global_command('Отобразить город', 'город [название города]')
    add_global_command('Зарегестрировать патент', 'рег ап')
    
    for desc, command in state['help']['global'].items():
        print_command(desc, command)
    