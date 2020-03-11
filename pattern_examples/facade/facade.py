#!/usr/bin/env python3

class Engine(object):

    def showEngineData(self):
        print("Nr silnika: {} Rok produkcji silnika: {}".format(43432331, 1995))

    def showEngineParameters(self):
        print("Moc: {} KM Skrzynia biegów: {}".format(150, "manualna"))


class Car(object):
    
    def __init__(self, engine, name):
        self.engine = engine
        self.speed = 0
        self.name = name
        self.onturn = ''

    def turn(self, trn):
        if trn == "left":
            print("Skręt w lewo")
        else:
            print("Skręt w prawo")
        self.onturn = trn

    def accelerate(self):
        self.speed += 1

    def show(self):
        print("Prędkość: {} Nazwa: {}".format(self.speed, self.name))

    def currentTurn(self):
        return self.onturn


class Facade(object):

    def __init__(self, car):
        self.car = car

    def showInfoAboutCar(self):
        car = self.car
        car.show()
        print("Skręt: {} Silnik: {}".format(car.currentTurn(), car.engine.showEngineData()))
        car.engine.showEngineParameters()

    def accelerate(self):
        self.car.accelerate()

    def turn(self, trn):
        self.car.turn(trn)


class Client(object):

    def go(self, fcd):
        fcd.accelerate()
        fcd.accelerate()
        fcd.turn("left")
        fcd.accelerate()
        fcd.showInfoAboutCar()
        print("")
        fcd.accelerate()
        fcd.showInfoAboutCar()
        print("")


if __name__ == '__main__':
    e1 = Engine()
    car1 = Car(e1, "Syrena")
    f1 = Facade(car1)
    cli1 = Client()
    cli1.go(f1)
