#!/usr/bin/env python3

class Position:
    def __init__(self, col_name, row):
        """Przechowuje pozycję na szachownicy"""
        if not ((col_name in "abcdefgh") and (1 <= row <= 8)):
            raise ValueError("Invalid position!")
        self._name = col_name
        self._row = row

    def get_coordinates(self):
        """Zwraca koordynaty z pozycji"""
        return self._name, self._row

    def __sub__(self, other_position):
        """Zwraca tuplę w postacji delty z pozycji bieżącej i przekazanej"""
        my_col, my_row = self.get_coordinates()
        other_col, other_row = other_position.get_coordinates()
        return ord(my_col) - ord(other_col), my_row - other_row

if __name__ == '__main__':
    position = Position('a', 2)
    try:
        position = Position('z', 9)
    except ValueError as e:
        print(e)

    print(Position('a', 1) - Position('b', 2))

