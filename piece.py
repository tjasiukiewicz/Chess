#!/usr/bin/env python3

from abc import abstractmethod
from color import Color
from position import Position
from piece_rules import *

class Piece:
    def __init__(self, rpr, color):
        """Inicjalizuje bierkę jej nazwą"""
        self._repr = rpr.lower()
        self._color = color

    def get_repr(self):
        """Zwraca literę z nazwą bierki"""
        return self._repr if self._color == Color.Black else self._repr.upper()

    def get_color(self):
        """Zwraca kolor bierki"""
        return self._color

    @abstractmethod
    def is_move_possible(self, from_position, to_position):
        """Zwraca informację o możliwości wykonania ruchu"""
        raise RuntimeError("Metoda abstrakcyjna")

class Pawn(Piece):

    def __init__(self, color):
        Piece.__init__(self, 'p', color)

    def is_move_possible(self, from_position, to_position):
        return (is_forward_move(from_position, to_position, self.get_color())
            and (is_two_row_move(from_position, to_position)
            or is_by_one_move(from_position, to_position)))

class Rook(Piece):

    def __init__(self, color):
        Piece.__init__(self, 'r', color)

    def is_move_possible(self, from_position, to_position):
        return is_same_row(from_position, to_position) or is_same_column(from_position, to_position)

class Knight(Piece):

    def __init__(self, color):
        Piece.__init__(self, 'n', color)

    def is_move_possible(self, from_position, to_position):
        return is_knight_move(from_position, to_position)

class Bishop(Piece):

    def __init__(self, color):
        Piece.__init__(self, 'b', color)

    def is_move_possible(self, from_position, to_position):
        return is_diagonal(from_position, to_position)

class Queen(Piece):

    def __init__(self, color):
        Piece.__init__(self, 'q', color)

    def is_move_possible(self, from_position, to_position):
        return (is_same_row(from_position, to_position) or is_same_column(from_position, to_position)
            or is_diagonal(from_position, to_position))

class King(Piece):

    def __init__(self, color):
        Piece.__init__(self, 'k', color)

    def is_move_possible(self, from_position, to_position):
        return is_by_one_move(from_position, to_position)
