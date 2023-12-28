state = {}

def reducer(action):
    match action.type:
        case 'REG_COPYRIGHT':
            player_name, transaction_hash, config = action
            for val in state.values():
                if val['player_name'] == player_name and transaction_hash in val['block']:
                    val['block'][transaction_hash] = config

def reg_copyright(player_name, transaction_hash, config):
    reducer({'type': 'REG_COPYRIGHT', 'player_name': player_name, 'transaction_hash': transaction_hash, 'config': config})
