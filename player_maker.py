#!/usr/bin/env python3

from color import Color
from player import Player
from console import Console

class PlayerMaker:
    def __init__(self, console = Console()):
        """Inicjalizuje obiekt fabrykujący przypisując konsolę"""
        self._console = console

    def make(self):
        """Tworzy 2 graczy, jako pierwszy zwracany z kolorem białym"""
        name1 = self._console.input_player_name(1)
        color1 = self._console.input_color(1)
        color2 = Color.Black if color1 == Color.White else Color.White
        name2 = self._console.input_player_name(2)
        player1 = Player(name1, color1)
        player2 = Player(name2, color2)
        return (player1, player2) if player1.get_color() == Color.White else (player2, player1)

if __name__ == '__main__':
    player1, player2 = PlayerMaker().make()
    print(player1.get_name(), player1.get_color())
    print(player2.get_name(), player2.get_color())
    assert(player1.get_color() == Color.White)
