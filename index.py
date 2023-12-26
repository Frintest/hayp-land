import curses

# DAL
cities = {}
path = '/'


def createCity(city):
    cities[city['name']] = city


# BLL
createCity(
    {
        'name': 'Гетто',
        'display_color': 'CYAN',
        'players': {
            'frunkers': {},
            'андрей': {}
        },
        'structures': {'банк': {}, 'суд': {}}
    }
)
createCity(
    {
        'name': 'Мультивёрс',
        'display_color': 'MAGENTA',
        'players': {
            'evgeny': {},
            'yoooou': {}
        },
        'structures': {'мафия': {}}
    }
)


def getColorPair(color_name):
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


def routing(stdscr):
    global path, cities

    def displayCities(stdscr, cities):
        for city_name, city_info in cities.items():
            stdscr.addstr(f"\n[{city_name}]\n", getColorPair(city_info['display_color']))

            def getCityItem(city_item):
                return ' | '.join(list(map(lambda item: item, city_item)))

            def printCityItem(city_item, title):
                stdscr.addstr(f'   {title}:\t')
                stdscr.addstr(f'{city_item}\n')

            printCityItem(getCityItem(city_info['players']), 'Жители')
            printCityItem(getCityItem(city_info['structures']), 'Структуры')

    if path == '/':
        stdscr.addstr('==== Города ==== \n')
        displayCities(stdscr, cities)
    elif '/ город:' in path:
        cities_copy = dict(filter(lambda item: item[0] == path[9:], cities.items()))
        displayCities(stdscr, cities_copy)
    elif path == '/ помощь':
        displayHelp(stdscr)


def displayHelp(stdscr):
    def printCommand(desc, command):
        stdscr.addstr(desc)
        stdscr.addstr(f'{command}\n', getColorPair('RED'))

    printCommand('Отобразить все города:\t', 'город *')
    printCommand('Отобразить город:\t', 'город [название города]')


def getCommand(stdscr):
    stdscr.addstr(f'\nДля отображения списка команд введите: помощь\n')
    stdscr.addstr(f'{path}\n', getColorPair('RED'))
    stdscr.addstr(':]', getColorPair('*WHITE_ON_RED'))
    stdscr.addstr(' ')
    return stdscr.getstr().decode('utf-8')


def changePath(command, path):
    if command[6:] in cities and command[:6] == 'город ':
        path = f'/ город: {command[6:]}'
    elif command == 'город *':
        path = '/'
    elif command == 'помощь':
        path = '/ помощь'
    return path


def loopCommand(stdscr):
    global path
    while True:
        stdscr.clear()
        routing(stdscr)
        command = getCommand(stdscr)
        path = changePath(command, path)
        stdscr.refresh()


# UI
def main(stdscr):
    curses.echo()
    curses.nocbreak()
    loopCommand(stdscr)


curses.wrapper(main)
