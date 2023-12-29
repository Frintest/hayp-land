from bll.routing_reducer import state as routing_state
from bll.cities_reducer import state as cities_state
from bll.patent_reducer import state as patent_state
from bll.help_reducer import state as help_state

state = {
    'routing': routing_state,
    'cities': cities_state,
    'patent': patent_state,
    'help': help_state
}
