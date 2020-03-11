#!/usr/bin/env python3.4

import random

class TestClass:

    def __init__(self):
        self._tm = None
        self._bProblem = 0

    def setup(self):
        print("Przygotowanie testu")
        self._tm.prepareReporting()

    def execute(self):
        if not self._bProblem:
            print("Wykonanie testu.")
        else:
            print("Error. Test nie jest uruchomiony.")

    def tearDown(self):
        if not self._bProblem:
            print("Czyszenie po teście.")
            self._tm.publishReport()
        else:
            print("Test nie został uruchomiony, zbędne czyszczenie po teście.")

    def setupTestManager(self, tm):
        self._tm = tm

    def setProblem(self, value):
        self._bProblem = value


class Reporter:

    def __init__(self):
        self._tm = None

    def prepare(self):
        print("Klasa Reporter, przygotowanie raportu testu.")

    def report(self):
        print("Raportowanie rezultatów testu.")

    def setupTestManager(self, tm):
        self._tm = tm


class DataBase:

    def __init__(self):
        self._tm = None

    def insert(self):
        print("Wstawienie informacji o rozpoczęciu testu do DataBase.")
        # Symulacja komunikacji od DataBase do TestClass
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print("Uaktualnienie rezultatów testu w DataBase")

    def setupTestManager(self, tm):
        self._tm = tm


class TestManager:

    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()

    def setReporter(self, reporter):
        self._reporter = reporter

    def setDataBase(self, db):
        self._db = db

    def publishReport(self):
        self._db.update()
        self._reporter.report()

    def setTestClass(self, tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DataBase()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDataBase(db)
    reporter.setupTestManager(tm)
    db.setupTestManager(tm)
    # Dla uproszczenia, pętla z tym samym testem.
    # W praktyce testy będą unikalne...
    for i in range(3):
        tc = TestClass()
        tc.setupTestManager(tm)
        tm.setTestClass(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()

