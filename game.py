#!/usr/bin/env python3

from player import Player
from chessboard import Chessboard
from color import Color

class Game:
    def __init__(self):
        """Inicjalizacja gry"""
        self._current_player = Player("Adam", Color.White)
        self._next_player = Player("Eve", Color.Black)
        self._board = Chessboard()
        self._board.init()

    def run(self):
        """Pętla główna gry"""
        self._board.draw()
        while True:
            try:
                position_from, position_to = self._current_player.get_move()
                self._board.move(position_from, position_to)
            except ValueError as e:
                print(e)
            else:
                self._current_player, self._next_player = self._next_player, self._current_player
                self._board.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
