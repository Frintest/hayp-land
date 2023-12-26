from ui.utilities.color_pair import setColorPair

def citiesPage(stdscr, cities):
    for city_name, city_info in cities.items():
        stdscr.addstr(f"\n[{city_name}]\n", setColorPair(city_info['display_color']))

        def getCityItem(city_item):
            return ' | '.join(list(map(lambda item: item, city_item)))

        def printCityItem(city_item, title):
            stdscr.addstr(f'   {title}:\t')
            stdscr.addstr(f'{city_item}\n')

        printCityItem(getCityItem(city_info['players']), 'Жители')
        printCityItem(getCityItem(city_info['structures']), 'Структуры')
