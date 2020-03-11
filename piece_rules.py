#!/usr/bin/env python3
from position import Position
from color import Color

def is_diagonal(from_positon, to_position):
    """Zwraca informację czy różnicą pozycji jest diagonalna

    >>> is_diagonal(Position('a', 1), Position('b', 2))
    True
    >>> is_diagonal(Position('e', 2), Position('e', 4))
    False
    """
    delta_col, delta_row = to_position - from_positon
    return abs(delta_col) == abs(delta_row)

def is_same_column(from_position, to_position):
    """Zwraca informację czy różnica pozycji jest w tej samej kolumnie

    >>> is_same_column(Position('b', 4), Position('b', 7))
    True
    >>> is_same_column(Position('e', 3), Position('f', 3))
    False
    """
    delta_col, delta_row = to_position - from_position
    return delta_col == 0

def is_same_row(from_position, to_position):
    """Zwraca informację czy różnica pozycji jest w tym samym wierszu

    >>> is_same_row(Position('d', 5), Position('f', 5))
    True
    >>> is_same_row(Position('a', 6), Position('a', 4))
    False
    """
    delta_col, delta_row = to_position - from_position
    return delta_row == 0

def is_forward_move(from_position, to_position, color):
    """Zwraca informację czy ruch jest wykonywany do przodu

    >>> is_forward_move(Position('e', 2), Position('e', 4), Color.White)
    True
    >>> is_forward_move(Position('e', 2), Position('e', 4), Color.Black)
    False
    >>> is_forward_move(Position('e', 7), Position('e', 6), Color.Black)
    True
    >>> is_forward_move(Position('e', 7), Position('e', 6), Color.White)
    False
    """
    delta_col, delta_row = to_position - from_position
    if color == Color.White and delta_row > 0:
        return True
    if color == Color.Black and delta_row < 0:
        return True
    return False

def is_by_one_move(from_position, to_position):
    """Zwraca informację czy ruch jest na pole sąsiednie

    >>> is_by_one_move(Position('a', 2), Position('b', 3))
    True
    >>> is_by_one_move(Position('b', 2), Position('a', 3))
    True
    >>> is_by_one_move(Position('f', 5), Position('e', 5))
    True
    >>> is_by_one_move(Position('e', 5), Position('f', 5))
    True
    >>> is_by_one_move(Position('e', 2), Position('e', 4))
    False
    >>> is_by_one_move(Position('e', 1), Position('e', 2))
    True
    """
    delta_col, delta_row = to_position - from_position
    return (delta_col == 0 and abs(delta_row) == 1
            or abs(delta_col) == 1 and delta_row == 0
            or abs(delta_col) == 1 and abs(delta_row) == 1)

def is_two_row_move(from_position, to_position):
    """Zwraca informację czy ruch jest o 2 wiersze

    >>> is_two_row_move(Position('e', 2), Position('e', 4))
    True
    >>> is_two_row_move(Position('d', 5), Position('d', 7))
    True
    >>> is_two_row_move(Position('e', 4), Position('e', 5))
    False
    >>> is_two_row_move(Position('b', 3), Position('c', 4))
    False
    """
    delta_col, delta_row = to_position - from_position
    return abs(delta_row) == 2

def is_knight_move(from_position, to_position):
    """Zwraca informację czy ruch jest ruchem skoczka

    >>> is_knight_move(Position('a', 2), Position('b', 4))
    True
    >>> is_knight_move(Position('b', 2), Position('a', 4))
    True
    >>> is_knight_move(Position('c', 5), Position('b', 3))
    True
    >>> is_knight_move(Position('c', 5), Position('d', 3))
    True
    >>> is_knight_move(Position('e', 2), Position('e', 4))
    False
    """
    delta_col, delta_row = to_position - from_position
    return ((abs(delta_row) == 1 and abs(delta_col) == 2)
            or (abs(delta_row) == 2 and abs(delta_col) == 1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

