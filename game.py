#!/usr/bin/env python3

from player import Player
from chessboard import Chessboard
from color import Color
from piece import *
from console import Console
from player_maker import PlayerMaker

class Game:
    def __init__(self, console = Console()):
        """Inicjalizacja gry"""
        self._console = console
        self._board = Chessboard()
        self._board.init()
        self._current_player, self._next_player = PlayerMaker(self._console).make()

    def run(self):
        """Pętla główna gry"""
        self._board.accept(self._console)
        self._console.draw()
        while True:
            try:
                position_from, position_to = self._current_player.get_move()
                piece = self._board.get_piece(position_from)
                if (piece.is_move_possible(position_from, position_to)
                        and piece.get_color() == self._current_player.get_color()):
                    self._board.move(position_from, position_to)
                else:
                    self._console.illegal_move_error()
                    continue
            except ValueError as e:
                print(e)
            else:
                self._current_player, self._next_player = self._next_player, self._current_player
                self._board.accept(self._console)
                self._console.draw()

if __name__ == '__main__':
    game = Game(Console())
    game.run()
