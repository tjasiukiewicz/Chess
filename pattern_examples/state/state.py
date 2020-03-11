#!/usr/bin/env python3

class State(object):

    """Stan bazowy, do dziedziczenia."""

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Skanowanie.. Stacja to:", self.stations[self.pos], self.name)


class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1120", "1310", "1460"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Przełączenie na FM")
        self.radio.state = self.radio.fmstate


class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["82.7", "83.1", "109.3"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Przełączenie na AM")
        self.radio.state = self.radio.amstate


class Radio(object):

    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions *= 2

    for action in actions:
        action()

