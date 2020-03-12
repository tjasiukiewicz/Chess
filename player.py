#!/usr/bin/env python3

from position import Position
from color import Color
from console import Console

class Player:
    def __init__(self, name, color, console = Console()):
        """Inicjalizacja gracza"""
        self._name = name
        self._color = color
        self._console = console

    def get_name(self):
        """Zwraca nazwę gracza"""
        return self._name

    def get_color(self):
        """Zwraca kolor gracza"""
        return self._color

    def get_move(self):
        """Pobranie poprawnego ruchu"""
        while True:
            self._console.show_player_info(self._name, self._color)
            from_col, from_row, to_col, to_row = self._console.input_move()
            from_row = int(from_row)
            to_row = int(to_row)
            if not (from_col in "abcdefgh" and 1 <= from_row <= 8 and to_col in "abcdefgh" and 1 <= to_row <= 8):
                self._console.illegal_move_error()
                continue
            return Position(from_col, from_row), Position(to_col, to_row)

if __name__ == '__main__':
    player = Player("Zenon", Color.White)
    print(player.get_move())
