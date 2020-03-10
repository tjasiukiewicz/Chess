#!/usr/bin/env python3

class Position:
    def __init__(self, col_name, row):
        """Przechowuje pozycję na szachownicy"""
        if not ((col_name in "abcdefgh") and (1 <= row <= 8)):
            raise ValueError("Invalid position!")
        self._name = col_name
        self._row = row

    def get_coordinates(self):
        return self._name, self._row

if __name__ == '__main__':
    position = Position('a', 2)
    try:
        position = Position('z', 9)
    except ValueError as e:
        print(e)

