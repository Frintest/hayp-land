from ui.utilities.color_pair import setColorPair

def reg_copyright_page(stdscr):
    stdscr.addstr('Для регистрации патента введите через пробел свой ')
    stdscr.addstr('hl_name', setColorPair('RED'))
    stdscr.addstr(' и ')
    stdscr.addstr('hl_pass\n', setColorPair('RED'))
    