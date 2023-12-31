from modules.gen_hash import check_valid_user, gen_hash

state = {}


def reducer(action):
    match action['type']:
        case 'ADD_PLAYER':
            state[action['user_name']] = {
                'user_name': action['user_name'],
                'user_hashpass': action['user_hashpass'],
                'patent_block': {}
            }
        
        case 'GET_HASH':
            for val in state.values():
                if check_valid_user(action['user_name'], action['user_pass'], state):
                    state[action['user_name']]['last_hash'] = gen_hash(action['user_pass'])
        
        case 'REG_PATENT':
            for val in state.values():
                if val['user_name'] == action['user_name']:
                    state[action['user_name']]['patent_block'][action['hash']] = {
                        'desc': action['desc']
                    }
        
        
def add_player_action(user_name, user_hashpass):
    reducer({'type': 'ADD_PLAYER', 'user_name': user_name, 'user_hashpass': user_hashpass})
    
add_player_action('f', 'a0b37b8bfae8e71330bd8e278e4a45ca916d00475dd8b85e9352533454c9fec8')


def get_hash_action(user_name, user_pass):
    reducer({'type': 'GET_HASH', 'user_name': user_name, 'user_pass': user_pass})
    

def reg_patent_action(user_name, patent_hash, desc):
    reducer({'type': 'REG_PATENT', 'user_name': user_name, 'hash': patent_hash, 'desc': desc})
