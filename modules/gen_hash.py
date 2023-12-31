from hashlib import sha3_256
from random import randint

def calculate_user_hashpass(user_pass):
    return sha3_256(user_pass.encode()).hexdigest()


def check_valid_user(user_name, user_pass, state):
    for val in state.values():
        if val['user_name'] == user_name and val['user_hashpass'] == calculate_user_hashpass(user_pass):
            return True
    return False


def calculate_mw_hash(user_pass):
    noise = str(randint(0, 9))
    in_str = user_pass + noise
    return {
        'mw_hash': sha3_256(in_str.encode()).hexdigest(),
        'noise': noise
    }


def calculate_hash(mw_hash, desc):
    in_str = mw_hash + desc
    return sha3_256(in_str.encode()).hexdigest()


#def is_chain_valid(chain, user_pass, desc):
    #for block_hash, block_data in chain.items():
        #if block_hash != gen_hash(user_pass, desc) or block_data['previous_hash'] != block_hash:
            #return False
    #return True
