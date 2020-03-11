#!/usr/bin/env python3

class Robaczek(object):

    def __init__(self, nr):
        self.nr_robaczka = nr
        print("Robaczek: Tworzenie robaczka o nr", nr)

    def __del__(self):
        print("Robaczek: Niszczenie robaczka o nr", self.nr_robaczka)

    def show(self):
        print("Robaczek: Tu robaczek o nr", self.nr_robaczka)


class WytworniaRobaczkow(object):
   
    def __init__(self):
        self.pula_robaczkow = []

    def getRobaczek(self, nr):
        # Naiwne szukanie liniowe
        for i in self.pula_robaczkow:
            if i.nr_robaczka == nr:
                return i
        print("Wytwórnia: Tworzenie robaczka o nr", nr)
        robaczek = Robaczek(nr)
        self.pula_robaczkow.append(robaczek)
        # TODO: Dodać ograniczenie wielkości puli robaczków
        return robaczek

    def showAll(self):
        for i in self.pula_robaczkow:
            i.show()

if __name__ == '__main__':
    w1 = WytworniaRobaczkow()
    print("Na początek 5 robaczków")
    print("-" * 20)
    for i in range(5):
        w1.getRobaczek(i).show()
    print("Teraz od 3 do 6")
    print("-" * 20)
    for i in range(3,7):
        w1.getRobaczek(i).show()
    print("I teraz wszystkie")
    print("-" * 20)
    w1.showAll()
    print("END MAIN")
    print("-" * 20)
    
