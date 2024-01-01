from bll.reducers.help import add_global_command

def create_help_commands():
    add_global_command('Отобразить все города', 'город *')
    add_global_command('Отобразить город', 'город [название города]')
    add_global_command('Зарегестрировать патент', 'рег ап')
