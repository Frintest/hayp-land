import curses
from routing.index import routing
from bll.routing_reducer import changePathAction, readCommandAction
from bll.cities_reducer import createCityAction
from ui.common.command import readCommand

createCityAction(
    {
        'name': 'АтлантCity',
        'display_color': 'CYAN',
        'players': {
            'frunkers': {},
            'кирилл': {}
        },
        'structures': {'Федеральное экономическое хранилище (ФЭХ)': {}}
    }
)


def render(stdscr):
    while True:
        stdscr.clear()
        routing(stdscr)
        readCommandAction(stdscr, readCommand(stdscr))
        changePathAction()
        stdscr.refresh()


def main(stdscr):
    curses.echo()
    curses.nocbreak()
    render(stdscr)


curses.wrapper(main)
