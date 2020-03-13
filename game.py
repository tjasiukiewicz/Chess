#!/usr/bin/env python3

from player import Player
from chessboard import Chessboard
from color import Color
from piece import *
from console import Console
from player_maker import PlayerMaker
import shelve

class Game:
    def __init__(self, console = Console()):
        """Inicjalizacja gry"""
        self._move_count = 0
        self._console = console
        self._board = Chessboard(self._console, self._console.draw)
        self._current_player, self._next_player = PlayerMaker(self._console).make()
        self._shelve = shelve.open("chessboard_move_storage", flag='n')

    def run(self):
        """Pętla główna gry"""
        self._board.init()
        self.save_state()
        while True:
            try:
                position_from, position_to = self._current_player.get_move()
                piece = self._board.get_piece(position_from)
                if (piece is not None and piece.is_move_possible(position_from, position_to)
                        and piece.get_color() == self._current_player.get_color()):
                    self._board.move(position_from, position_to)
                else:
                    self._console.illegal_move_error()
                    continue
                self._move_count += 1
                self.save_state()
                self._swap_players()
            except ValueError as e:
                if e.args[0] == 'n':
                    # Next move
                    if str(self._move_count + 1) in (self._shelve.keys()):
                        self._move_count += 1
                        self.restore_state()
                        self._board_presentation()
                        #if not (self._move_count % 2):
                        self._swap_players()
                    else:
                        self._console.show_is_not_next_move()
                elif e.args[0] == 'p':
                    # Prev move
                    if str(self._move_count - 1) in (self._shelve.keys()):
                        self._move_count -= 1
                        self.restore_state()
                        self._board_presentation()
                        #if self._move_count % 2:
                        self._swap_players()
                    else:
                        self._console.show_is_not_prev_move()
                else:
                    print(e)

    def restore_state(self):
        """Odtwarza stan gry"""
        self._current_player, self._next_player, self._board = self._shelve[str(self._move_count)]

    def save_state(self):
        """Zapisuje stan gry"""
        self._shelve[str(self._move_count)] = (self._current_player, self._next_player, self._board)

    def _swap_players(self):
        """Zamienia graczy"""
        self._current_player, self._next_player = self._next_player, self._current_player

    def _board_presentation(self):
        # FIXME: It's temporary solution
        self._board._accept(self._board._console)
        self._board._change_state_call()


if __name__ == '__main__':
    game = Game(Console())
    game.run()
