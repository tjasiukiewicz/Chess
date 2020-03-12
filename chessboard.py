#!/usr/bin/env python3
"""Moduł obsługujący szachownicę do gry w tradycyjne szachy"""

from piece import *
from position import Position
from color import Color
from console import Console

piece_to_value = { Pawn: 1, Rook: 2, Knight: 3, Bishop: 4, Queen: 5, King: 6 }

class Chessboard:
    def __init__(self, console = Console(), change_state_call = lambda: 0):
        """Inicjalizuje pustą szachownicę"""
        self._fields = { row: { col: None for col in 'abcdefgh'}
                for row in range(1, 9)}
        self._console = console
        self._change_state_call = change_state_call

    def init(self):
        """Ustawia figury w początkowym stanie"""
        for col in "abcdefgh":
            self._fields[7][col] = Pawn(Color.Black)
            self._fields[2][col] = Pawn(Color.White)
        for col, piece in zip('abcdefgh', (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
            self._fields[1][col] = piece(Color.White)
            self._fields[8][col] = piece(Color.Black)
        self._accept(self._console)
        self._change_state_call()

    def move(self, position_from, position_to):
        """Przesuwa pionek na polach"""
        # TODO: Tak naprawdę, ruch może posiadać status więc raczej
        #       powinien zwracać enum a nie Bool.
        from_col, from_row = position_from.get_coordinates()
        to_col, to_row = position_to.get_coordinates()
        from_field = self._fields[from_row][from_col]
        to_field = self._fields[to_row][to_col]
        if from_field is not None and to_field is None:
            self._fields[to_row][to_col] = from_field
            self._fields[from_row][from_col] = None
            self._accept(self._console)
            self._change_state_call()
            return True
        else:
            raise ValueError("Invalid move!")
        return False

    def get_piece(self, position):
        """Zwraca pionek na danej pozycji"""
        col, row = position.get_coordinates()
        return self._fields[row][col]

    def _accept(self, console):
        """Zasila danymi wizytator console"""
        data = [[self._transform(row, col) for col in "abcdefgh"] for row in range(8, 0, -1)]
        console.visit(data)

    def _transform(self, row, col):
        field = self._fields[row][col]
        value = 0
        if field != None:
            value = piece_to_value[field.__class__]
            value += 0 if self._fields[row][col].get_color() == Color.White else 100
        return value


if __name__ == '__main__':
    chessboard = Chessboard()
    console = Console()
    chessboard.accept(console)
    console.draw()
    chessboard.init()
    chessboard.accept(console)
    console.draw()


