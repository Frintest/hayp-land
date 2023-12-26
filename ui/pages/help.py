from ui.utilities.color_pair import setColorPair

def helpPage(stdscr):
    def printCommand(desc, command):
        stdscr.addstr(desc)
        stdscr.addstr(f'{command}\n', setColorPair('RED'))
        
    printCommand('Отобразить все города:\t', 'город *')
    printCommand('Отобразить город:\t', 'город [название города]')