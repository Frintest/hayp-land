from ui.utilities.color_pair import set_color_pair
from bll.reducers.users import calculate_mw_hash_action, create_patent_action, create_user_action, is_chain_valid_action
from bll.state import state

def patent_page():
    print(set_color_pair('RESET') + 'Для регистрации патента введите через пробел свой ', end='')
    print(set_color_pair('APP') + 'user_name' + set_color_pair('RESET') + ' и ' + set_color_pair('APP') + 'user_hashpass')
    
    create_user_action('f', 'a0b37b8bfae8e71330bd8e278e4a45ca916d00475dd8b85e9352533454c9fec8')
    create_patent_action('f', 'a0b37b8bfae8e71330bd8e278e4a45ca916d00475dd8b85e9352533454c9fec8' ,'первое описание')
    #state['users']['f']['patent_chain'][0]['hash'] = 'aboba'
    is_chain_valid_action('f', 'f')
    print(state['users']['f']['is_valid'])
    
    print(state['users']['f']['patent_chain'])
    if state['routing']['command'] != 'рег ап':
        try:
            user_name, user_pass = state['routing']['command'].split(' ')
            calculate_mw_hash_action(user_name, user_pass)
            print(set_color_pair('RESET') + 'Скопируйте промежуточный хеш: ', end='')
            print(set_color_pair('APP') + state['users'][user_name]['last_hash'])
            print(state['users'][user_name])
        except:
            print(set_color_pair('RED') + 'ERR: Неверная команда или формат входных данных\n', end='')
    