from hashlib import sha3_256
from random import randint


def calculate_user_hashpass(user_pass: str) -> str:
    return sha3_256(user_pass.encode()).hexdigest()


def calculate_mw_hash(user_pass: str):
    in_str = user_pass
    return {
        'mw_hash': sha3_256(in_str.encode()).hexdigest(),
    }


def calculate_hash(mw_hash: str, previous_hash: str, desc: str) -> str:
    in_str = mw_hash + previous_hash + desc
    return sha3_256(in_str.encode()).hexdigest()
