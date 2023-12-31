import hashlib

def check_valid_user(user_name, user_pass, state):
    for val in state.values():
        if val['user_name'] == user_name and val['user_hashpass'] == gen_hash(user_pass):
            isValid = True
            break
        else:
            isValid = False
    return isValid


def gen_hash(user_pass):
    return hashlib.sha3_256(user_pass.encode()).hexdigest()
