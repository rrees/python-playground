from .commands import action_mapper


def parse(user_input):
    # Split the input into words
    words = user_input.lower().split()
    if not words:
        print("No command entered.")
        return

    # The first word is the command
    command = words[0]
    # The rest are arguments
    parameters = words[1:]

    return (command, action_mapper(command), parameters)
