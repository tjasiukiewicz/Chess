#!/usr/bin/env python3

from color import Color

class Piece:
    def __init__(self, rpr, color):
        """Inicjalizuje bierkę jej nazwą"""
        self._repr = rpr.lower()
        self._color = color

    def get_repr(self):
        """Zwraca literę z nazwą bierki"""
        return self._repr if self._color == Color.Black else self._repr.upper()

    def get_color(self):
        return self._color
