#!/usr/bin/env python3

from game import Game
from console import Console

if __name__ == '__main__':
    console = Console()
    game = Game(console)
    game.run()
