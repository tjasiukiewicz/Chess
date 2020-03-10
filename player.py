#!/usr/bin/env python3

from position import Position
from color import Color

class Player:
    def __init__(self, name, color):
        """Inicjalizacja gracza"""
        self._name = name
        self._color = color

    def get_name(self):
        """Zwraca nazwę gracza"""
        return self._name

    def get_color(self):
        """Zwraca kolor gracza"""
        return self._color

    def get_move(self):
        """Pobranie poprawnego ruchu"""
        while True:
            print("Player: %s, plays: %s" % (self._name, self._color), end='')
            from_col, from_row, to_col, to_row = input(" move: ")
            from_row = int(from_row)
            to_row = int(to_row)
            if not (from_col in "abcdefgh" and 1 <= from_row <= 8 and to_col in "abcdefgh" and 1 <= to_row <= 8):
                print("Position Error! Try again!")
                continue
            return Position(from_col, from_row), Position(to_col, to_row)

if __name__ == '__main__':
    player = Player("Zenon", Color.White)
    print(player.get_move())
