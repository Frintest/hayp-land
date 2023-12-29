state = {
    'f': {
        'hl_name': 'f',
        'block': {
            'f': ''
        }
    }
}


def reducer(action):
    match action['type']:
        case 'REG_PATENT':
            for val in state.values():
                if val['hl_name'] == action['hl_name'] and action['hash'] in val['block']:
                    state[action['hl_name']]['block'][action['hash']] = action['config']

def reg_patent_action(hl_name, transaction_hash, config):
    reducer({'type': 'REG_PATENT', 'hl_name': hl_name, 'hash': transaction_hash, 'config': config})
