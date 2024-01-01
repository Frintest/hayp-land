from modules.gen_hash import is_user_valid, calculate_mw_hash, calculate_hash, is_chain_valid

state = {}


def reducer(action):
    match action['type']:
        case 'CREATE_USER':
            state[action['user_name']] = {
                'user_name': action['user_name'],
                'user_hashpass': action['user_hashpass'],
                'patent_chain': [
                    {
                        'hash': '0',
                        'desc': 'Genesis block'
                    }
                ]
            }
        
        case 'CALCULATE_MW_HASH_ACTION':
            for val in state.values():
                if is_user_valid(action['user_name'], action['user_pass'], state):
                    res = calculate_mw_hash(action['user_pass'])
                    state[action['user_name']]['last_hash'] = res['mw_hash']
                    #state[action['user_name']]['noise'] = res['noise']
                    
        
        case 'CREATE_PATENT':
            def is_user_name_valid():
                for val in state.values():
                    if val['user_name'] == action['user_name']:
                        return True
                return False
            
            if is_user_name_valid():
                chain = state[action['user_name']]['patent_chain']
                chain.append({
                    'hash': calculate_hash(action['mw_hash'], chain[-1]['hash'], action['desc']),
                    'previous_hash': chain[-1]['hash'],
                    'desc': action['desc']
                })
                
        case 'IS_CHAIN_VALID':
            if is_user_valid(action['user_name'], action['user_pass'], state):
                state[action['user_name']]['is_valid'] = is_chain_valid(state[action['user_name']]['patent_chain'], action['user_pass'])
        
        
def create_user_action(user_name, user_hashpass):
    reducer({'type': 'CREATE_USER', 'user_name': user_name, 'user_hashpass': user_hashpass})


def calculate_mw_hash_action(user_name, user_pass):
    reducer({'type': 'CALCULATE_MW_HASH_ACTION', 'user_name': user_name, 'user_pass': user_pass})


def create_patent_action(user_name, mw_hash, desc):
    reducer({'type': 'CREATE_PATENT', 'user_name': user_name, 'mw_hash': mw_hash, 'desc': desc})


def is_chain_valid_action(user_name, user_pass):
    reducer({'type': 'IS_CHAIN_VALID', 'user_name': user_name, 'user_pass': user_pass})
