from bll.state import state
from ui.utilities.color_pair import setColorPair

def readCommand(stdscr):
    stdscr.addstr(f'\nДля отображения списка команд введите: помощь\n')
    stdscr.addstr(f'{state["routing"]["path"]}\n', setColorPair('RED'))
    stdscr.addstr(':]', setColorPair('*WHITE_ON_RED'))
    stdscr.addstr(' ')
    return stdscr.getstr().decode('utf-8')
