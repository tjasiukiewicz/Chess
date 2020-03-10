#!/usr/bin/env python3
"""Moduł obsługujący szachownicę do gry w tradycyjne szachy"""

from piece import Piece

class Chessboard:
    def __init__(self):
        """Inicjalizuje pustą szachownicę"""
        self._fields = { row: { col: None for col in 'abcdefgh'}
                for row in range(1, 9)}

    def init(self):
        """Ustawia figury w początkowym stanie"""
        for col in "abcdefgh":
            self._fields[7][col] = Piece('p')
            self._fields[2][col] = Piece('P')
        for col, name in zip('abcdefgh', 'rnbqkbnr'):
            self._fields[1][col] = Piece(name.upper())
            self._fields[8][col] = Piece(name)

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

if __name__ == '__main__':
    # US1
    chessboard = Chessboard()
    chessboard.draw()
    # US2
    chessboard.init()
    chessboard.draw()


