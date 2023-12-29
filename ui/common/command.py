from bll.state import state
from ui.utilities.color_pair import set_color_pair

def read_command():
    print(set_color_pair('RESET') + f'\nДля отображения списка команд введите: помощь')
    print(set_color_pair('APP') + f'{state["routing"]["path"]}\n$ ', end='')
    return input()
