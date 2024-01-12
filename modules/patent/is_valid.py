from modules.cities.calculate_hash import calculate_user_hashpass, calculate_mw_hash, calculate_hash


def is_user_valid(user_name: str, user_pass: str, state: dict) -> bool:
    if user_name in state.keys() and state[user_name]['user_hashpass'] == calculate_user_hashpass(user_pass):
        return True
    return False


def is_chain_valid(chain: dict, user_pass: str) -> bool:
    for i in range(1, len(chain)):
        mw_hash = calculate_mw_hash(user_pass)
        block_hash = calculate_hash(mw_hash['mw_hash'], chain[i]['previous_hash'], chain[i]['desc'])
        if chain[i]['hash'] != block_hash or chain[i]['previous_hash'] != chain[i - 1]['hash']:
            return False
    return True
