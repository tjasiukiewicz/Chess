#!/usr/bin/env python3

class Piece:
    def __init__(self, rpr):
        """Inicjalizuje bierkę jej nazwą"""
        # TODO: A czy bierka nie powinna mieć przypadkiem koloru?
        self._repr = rpr

    def get_repr(self):
        """Zwraca literę z nazwą bierki"""
        return self._repr
