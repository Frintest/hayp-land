from modules.cities.calculate_hash import calculate_mw_hash, calculate_hash
from modules.cities.is_valid import is_user_valid, is_chain_valid


state = {}


def reducer(action: dict):
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
            if is_user_valid(action['user_name'], action['user_pass'], state):
                res = calculate_mw_hash(action['user_pass'])
                state[action['user_name']]['draft_hash'] = res['mw_hash']
                #state[action['user_name']]['noise'] = res['noise']
                
        
        case 'CREATE_PATENT':
            if state[action['user_name']]:
                chain = state[action['user_name']]['patent_chain']
                chain.append({
                    'hash': calculate_hash(action['mw_hash'], chain[-1]['hash'], action['desc']),
                    'previous_hash': chain[-1]['hash'],
                    'desc': action['desc']
                })
                
                
        case 'IS_CHAIN_VALID':
            if is_user_valid(action['user_name'], action['user_pass'], state):
                state[action['user_name']]['is_chain_valid'] = is_chain_valid(state[action['user_name']]['patent_chain'], action['user_pass'])
                
                
        case 'IS_USER_VALID':
            if is_user_valid(action['user_name'], action['user_pass'], state):
                state['is_user_valid'] = True
            else:
                state['is_user_valid'] = False
        
        
def create_user_action(user_name: str, user_hashpass: str):
    reducer({'type': 'CREATE_USER', 'user_name': user_name, 'user_hashpass': user_hashpass})


def calculate_mw_hash_action(user_name: str, user_pass: str):
    reducer({'type': 'CALCULATE_MW_HASH_ACTION', 'user_name': user_name, 'user_pass': user_pass})


def create_patent_action(user_name: str, mw_hash: str, desc: str):
    reducer({'type': 'CREATE_PATENT', 'user_name': user_name, 'mw_hash': mw_hash, 'desc': desc})


def is_chain_valid_action(user_name: str, user_pass: str):
    reducer({'type': 'IS_CHAIN_VALID', 'user_name': user_name, 'user_pass': user_pass})


def is_user_valid_action(user_name: str, user_pass: str):
    reducer({'type': 'IS_USER_VALID', 'user_name': user_name, 'user_pass': user_pass})
