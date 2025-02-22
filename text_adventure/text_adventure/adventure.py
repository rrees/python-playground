from . import parser
from .game.game import Game
from .player import Player


def adventure():
    print("Text adventure")

    player = Player()
    game = Game(playing=True)

    while game.playing:
        user_input = input("> ")
        command, action, parameters = parser.parse(user_input)

        if not action:
            print(f"Command not recognised: {command}")
            continue

        (response,) = action(game, player, parameters)

        print(response)
