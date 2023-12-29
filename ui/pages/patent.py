from ui.utilities.color_pair import setColorPair
from bll.patent_reducer import reg_patent_action
from bll.state import state

def patent_page(stdscr):
    stdscr.addstr('Для регистрации патента введите через пробел свой ')
    stdscr.addstr('hl_name', setColorPair('RED'))
    stdscr.addstr(' и ')
    stdscr.addstr('hl_pass\n', setColorPair('RED'))
    hl_name, hl_pass = state['routing']['command'].split(' ')
    reg_patent_action(hl_name, hl_pass, 'yes')
    stdscr.addstr(state['patent']['f']['block']['f'])
    