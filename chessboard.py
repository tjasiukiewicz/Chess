#!/usr/bin/env python3
"""Moduł obsługujący szachownicę do gry w tradycyjne szachy"""

from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from position import Position
from color import Color

class Chessboard:
    def __init__(self):
        """Inicjalizuje pustą szachownicę"""
        self._fields = { row: { col: None for col in 'abcdefgh'}
                for row in range(1, 9)}

    def init(self):
        """Ustawia figury w początkowym stanie"""
        for col in "abcdefgh":
            self._fields[7][col] = Pawn(Color.Black)
            self._fields[2][col] = Pawn(Color.White)
        for col, piece in zip('abcdefgh', (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
            self._fields[1][col] = piece(Color.White)
            self._fields[8][col] = piece(Color.Black)

    def draw(self):
        """Wyświetla szachownicę"""
        self._show_column_names()
        for row in range(8, 0, -1):
            self._show_row_separator()
            self._show_row(row)
        self._show_row_separator()
        self._show_column_names()

    def _show_column_names(self):
        """Wyświetla nazwy kolumn"""
        print("   a b c d e f g h")

    def _show_row_separator(self):
        """Wyświetla separator wierszy"""
        print("  ", "+-" * 8, '+', sep='')

    def _show_row(self, row):
        """Wyświetla pełen wiersz z figurami"""
        print(row, end=' ')
        for col in 'abcdefgh':
            field = self._fields[row][col]
            rpr = ' ' if field == None else field.get_repr()
            print('|', rpr, sep='', end='')
        print('|', row)

    def move(self, position_from, position_to):
        """Przesuwa pionek na polach"""
        from_col, from_row = position_from.get_coordinates()
        to_col, to_row = position_to.get_coordinates()
        from_field = self._fields[from_row][from_col]
        to_field = self._fields[to_row][to_col]
        if to_field is None and from_field is not None:
            self._fields[to_row][to_col] = from_field
            self._fields[from_row][from_col] = None
        else:
            raise ValueError("Invalid move!")

    def get_piece(self, position):
        """Zwraca pionek na danej pozycji"""
        col, row = position.get_coordinates()
        return self._fields[row][col]

if __name__ == '__main__':
    # US1
    chessboard = Chessboard()
    chessboard.draw()
    # US2
    chessboard.init()
    chessboard.draw()
    # US3
    from_position = Position('e', 2)
    to_position = Position('e', 4)
    if chessboard.move(from_position, to_position):
        print("Move SUCCESS!")
    else:
        print("Move FAIL!!")
    chessboard.draw()


