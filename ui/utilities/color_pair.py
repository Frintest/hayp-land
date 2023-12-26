import curses

def setColorPair(color_name):
    if color_name == 'WHITE':
        pair_num = 1
        curses.init_pair(pair_num, curses.COLOR_WHITE, curses.COLOR_BLACK)
    elif color_name == 'MAGENTA':
        pair_num = 2
        curses.init_pair(pair_num, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    elif color_name == 'YELLOW':
        pair_num = 3
        curses.init_pair(pair_num, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    elif color_name == 'RED':
        pair_num = 4
        curses.init_pair(pair_num, curses.COLOR_RED, curses.COLOR_BLACK)
    elif color_name == 'GREEN':
        pair_num = 5
        curses.init_pair(pair_num, curses.COLOR_GREEN, curses.COLOR_BLACK)
    elif color_name == 'BLUE':
        pair_num = 6
        curses.init_pair(pair_num, curses.COLOR_BLUE, curses.COLOR_BLACK)
    elif color_name == 'CYAN':
        pair_num = 7
        curses.init_pair(pair_num, curses.COLOR_CYAN, curses.COLOR_BLACK)
    elif color_name == '*WHITE_ON_RED':
        pair_num = 100
        curses.init_pair(pair_num, curses.COLOR_WHITE, curses.COLOR_RED)
    return curses.color_pair(pair_num)
