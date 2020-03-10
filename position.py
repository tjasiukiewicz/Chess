#!/usr/bin/env python3

class Position:
    def __init__(self, col_name, row):
        """Przechowuje pozycję na szachownicy"""
        assert((col_name in "abcdefgh") and (1 <= row <= 8))
        self._name = col_name
        self._row = row

    def get_coordinates(self):
        return self._name, self._row

if __name__ == '__main__':
    position = Position('a', 9)

