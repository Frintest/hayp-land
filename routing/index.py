from ui.pages.help.index import help_page
from ui.pages.cities.index import cities_page
from ui.pages.patent.index import patent_page
from bll.state import state
from ui.utilities.color_pair import set_color_pair

def routing():
    path = state['routing']['path']
    cities = state['cities']['cities']
    
    if path == '/':
        print(set_color_pair('RESET') + '==== Города ====\n')
        cities_page(cities)
    elif '/ город:' in path:
        cities_page(dict(filter(lambda item: item[0] == path[9:], cities.items())))
    elif path == '/ помощь':
        help_page()
    elif path == '/ рег ап':
        patent_page()
