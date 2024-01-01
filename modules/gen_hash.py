from hashlib import sha3_256
from random import randint

def calculate_user_hashpass(user_pass):
    return sha3_256(user_pass.encode()).hexdigest()


def is_user_valid(user_name, user_pass, state):
    for val in state.values():
        if val['user_name'] == user_name and val['user_hashpass'] == calculate_user_hashpass(user_pass):
            return True
    return False


def calculate_mw_hash(user_pass):
    #noise = str(randint(0, 9))
    in_str = user_pass
    return {
        'mw_hash': sha3_256(in_str.encode()).hexdigest(),
        #'nonce': noise
    }


def calculate_hash(mw_hash, previous_hash, desc):
    in_str = mw_hash + previous_hash + desc
    return sha3_256(in_str.encode()).hexdigest()


def is_chain_valid(chain, user_pass):
    for i in range(1, len(chain)):
        mw_hash = calculate_mw_hash(user_pass)
        block_hash = calculate_hash(mw_hash['mw_hash'], chain[i]['previous_hash'], chain[i]['desc'])
        if chain[i]['hash'] != block_hash or chain[i]['previous_hash'] != chain[i - 1]['hash']:
            return False
    return True
