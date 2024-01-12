from bll.reducers.routing import state as routing_state
from bll.reducers.cities import state as cities_state
from bll.reducers.users import state as users_state
from bll.reducers.help import state as help_state


state = {
    'routing': routing_state,
    'cities': cities_state,
    'users': users_state,
    'help': help_state,
}
