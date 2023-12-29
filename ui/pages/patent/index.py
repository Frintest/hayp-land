from ui.utilities.color_pair import set_color_pair
from bll.patent_reducer import reg_patent_action
from bll.state import state

def patent_page():
    print(set_color_pair('RESET') + 'Для регистрации патента введите через пробел свой ', end='')
    print(set_color_pair('APP') + 'hl_name' + set_color_pair('RESET') + ' и ' + set_color_pair('APP') + 'hl_pass')
    hl_name, hl_pass = state['routing']['command'].split(' ')
    reg_patent_action(hl_name, hl_pass, 'yes')
    print(state['patent']['f']['block']['f'])
    