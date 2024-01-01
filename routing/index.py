from ui.pages.help.index import help_page
from ui.pages.cities.index import cities_page
from ui.pages.patent.index import patent_page
from bll.state import state

def routing():
    path = state['routing']['path']
    path_prefix = state['routing']['path_prefix']
    cities = state['cities']['cities']
    
    if path == '/':
        cities_page(cities)
        
    elif f'{path_prefix}город:' in path:
        cities_page(dict(filter(lambda item: item[0] == path[len(f'{path_prefix}город: '):], cities.items())))
        
    elif path == f'{path_prefix}помощь':
        help_page()
        
    elif path == f'{path_prefix}рег ап':
        patent_page()
