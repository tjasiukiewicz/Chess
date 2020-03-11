#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
class AnswerStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def answer(self, ask):
        pass

class AskMom(AnswerStrategy):

    def answer(self, ask):
        if ask == "Skąd się biorą dzieci?":
            return "Bocian przynosi."
        else:
            return ""

class AskDad(AnswerStrategy):

    def answer(self, ask):
        if ask == "Dziadku, daj mi 10 PLN na lody.":
            return "Masz tu 10 PLN, ale nie mów babci."
        else:
            return ""

class AskGrandmama(AnswerStrategy):

    def answer(self, ask):
        if ask == "A Dziadek je cukierki.":
            return "Oj ten głupi piernik."
        else:
            return ""

class Question(AnswerStrategy):

    def __init__(self):
        answers = []
        # XXX: Tu można sterować kolejnością wykonywania zapytań.
        answers.append(AskMom())
        answers.append(AskDad())
        answers.append(AskGrandmama())
        self.answers = answers

    def answer(self, ask):
        # Odpowiedź od 1 poprawnego
        for i in self.answers:
            if i.answer(ask) != "":
                # FIXME: Trochę niewydajne jeszcze raz pytać... :-/
                return i.answer(ask)
        return "Buu... nikt nie wie...\n"

if __name__ == '__main__':
    q = Question()
    print(q.answer("Co oznacza 42?"))
