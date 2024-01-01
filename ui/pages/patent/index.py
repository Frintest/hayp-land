from ui.utilities.color_pair import set_color_pair
from bll.reducers.users import calculate_mw_hash_action, create_patent_action, is_chain_valid_action, is_user_valid_action
from bll.state import state

def patent_page():
    print(set_color_pair('RESET') + 'Для регистрации патента введите через пробел свой ', end='')
    print(set_color_pair('APP') + 'user_name' + set_color_pair('RESET') + ' и ' + set_color_pair('APP') + 'user_hashpass')
    #state['users']['f']['patent_chain'][0]['hash'] = 'aboba'
    #is_chain_valid_action('f', 'f')

    if state['routing']['command'] != 'рег ап':
        try:
            user_name, user_pass = state['routing']['command'].split(' ')
            is_user_valid_action(user_name, user_pass)
            print(state['users'])
            
            if state['users']['is_user_valid']:
                calculate_mw_hash_action(user_name, user_pass)
                print(set_color_pair('RESET') + 'Скопируйте промежуточный хеш: ', end='')
                print(set_color_pair('APP') + state['users'][user_name]['last_hash'])
            else:
                print(set_color_pair('RED') + 'ERR: Неверные данные пользователя')
        except:
            print(set_color_pair('RED') + 'ERR: Несуществующая команда или неверный формат входных данных\n', end='')
    