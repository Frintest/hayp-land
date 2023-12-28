from ui.utilities.color_pair import setColorPair
from bll.help_reducer import add_global_command
from bll.state import state

def helpPage(stdscr):
    def printCommand(desc, command):
        stdscr.addstr(f'{desc:<27}')
        stdscr.addstr(f'{command}\n', setColorPair('RED'))
    
    add_global_command('Отобразить все города', 'город *')
    add_global_command('Отобразить город', 'город [название города]')
    add_global_command('Зарегестрировать патент', 'рег ап')
    
    for desc, command in state['help']['global'].items():
        printCommand(desc, command)
    
    