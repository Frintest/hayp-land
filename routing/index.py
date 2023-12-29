from ui.pages.help import help_page
from ui.pages.cities import cities_page
from ui.pages.patent import patent_page
from bll.state import state
from ui.utilities.color_pair import set_color_pair

def routing():
    path = state['routing']['path']
    cities = state['cities']['cities']
    
    if path == '/':
        print(set_color_pair('RESET') + '==== Города ====\n')
        cities_page(cities)
    elif '/ город:' in path:
        cities_copy = dict(filter(lambda item: item[0] == path[9:], cities.items()))
        cities_page(cities_copy)
    elif path == '/ помощь':
        help_page()
    elif path == '/ рег ап':
        patent_page()
