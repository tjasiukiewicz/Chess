#!/usr/bin/env python3

class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        # FIXME: Pamiętaj "dziecko"! Tak się nie robi :-)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# Przykładowe użycie, wywołanie akcji... 
class Data(Subject):

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:

    def update(self, subject):
        print('HexViewer: Podmiot %s ma dane 0x%x' %
              (subject.name, subject.data))


class DecimalViewer:

    def update(self, subject):
        print('DecimalViewer: Podmiot %s ma dane %d' %
              (subject.name, subject.data))


if __name__ == '__main__':
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)

    print("Dane 1 = 10")
    data1.data = 10
    print("Dane 2 = 15")
    data2.data = 15
    print("Dane 1 = 3")
    data1.data = 3
    print("Dane 2 = 5")
    data2.data = 5
    print("Odłączenie HexViewer z data1 i data2.")
    data1.detach(view2)
    data2.detach(view2)
    print("Dane 1 = 10")
    data1.data = 10
    print("Dane 2 = 15")
    data2.data = 15

