from colorama import Fore


def set_color_pair(color_name: str):
    match color_name:
        case 'APP':
            color_out = Fore.LIGHTGREEN_EX
        case 'RESET':
            color_out = Fore.RESET
        case 'RED':
            color_out = Fore.RED
        case 'GREEN':
            color_out = Fore.GREEN
        case 'BLUE':
            color_out = Fore.BLUE
        case 'YELLOW':
            color_out = Fore.YELLOW
        case 'MAGENTA':
            color_out = Fore.MAGENTA
        case 'CYAN':
            color_out = Fore.CYAN
        case 'WHITE':
            color_out = Fore.WHITE

    return color_out
