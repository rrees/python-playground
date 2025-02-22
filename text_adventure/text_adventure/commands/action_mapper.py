from .look import look
from .quit import quit

commands_with_aliases = ((("look", "l"), look), (("q", "quit", "exit"), quit))

valid_commands = {
    alias: command_function
    for aliases, command_function in commands_with_aliases
    for alias in aliases
}


def action_mapper(command):
    command_function = valid_commands.get(command, None)

    return command_function
