from ui.utilities.color_pair import set_color_pair
from ui.pages.cities.city import city


def cities_page(cities):
    if len(cities.keys()) != 1:
        print(set_color_pair('RESET') + '==== Города ====\n')
    
    for city_name, city_info in cities.items():
        city(city_name, city_info)
    