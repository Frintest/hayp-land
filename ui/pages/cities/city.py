from ui.utilities.color_pair import set_color_pair


def city(city_name: str, city_info: dict):
    print(set_color_pair(city_info['display_color']) + f"[{city_name}]")
    
    def get_city_item(city_item: dict):
        return ' | '.join(list(map(lambda item: item, city_item)))
    
    
    def print_city_item(title: str, city_item: dict):
        print(set_color_pair('RESET') + f'   {title + ":":<15}{get_city_item(city_item)}')
    
    
    print_city_item('Жители', city_info['users'])
    print_city_item('Структуры', city_info['structures'])
