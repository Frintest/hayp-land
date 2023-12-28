from ui.pages.help import helpPage
from ui.pages.cities import citiesPage
from ui.pages.reg_copyright import reg_copyright_page
from bll.state import state

def routing(stdscr):
    path = state['routing']['path']
    cities = state['cities']['cities']
    
    if path == '/':
        stdscr.addstr('==== Города ==== \n')
        citiesPage(stdscr, cities)
    elif '/ город:' in path:
        cities_copy = dict(filter(lambda item: item[0] == path[9:], cities.items()))
        citiesPage(stdscr, cities_copy)
    elif path == '/ помощь':
        helpPage(stdscr)
    elif path == '/ рег ап':
        reg_copyright_page(stdscr)
