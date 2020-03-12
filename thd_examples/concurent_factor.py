#!/usr/bin/env python3
import time
import random
from multiprocessing import Process

# Faktoryzacja dla 'n'
def calculatePrimeFactors(n):
    primfac = []
    d= 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d) # Będą powtórzenia dla dzielników
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

def executeProc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculatePrimeFactors(rand))

# Dzielenie pracy dla 10 000 obliczeń
# na dziesięć prac po 1 000 obliczeń
def main():
    print("Start obliczeń")
    t0 = time.time()
    procs = []
    # Kreowanie procesów i ich uruchomienie
    for i in range(10):
        proc = Process(target=executeProc, args=())
        procs.append(proc)
        proc.start()
    # Przyłączanie procesów
    for proc in procs:
        proc.join()
    t1 = time.time()
    totalTime = t1 - t0
    # Prezentacja czasu wykonania
    print("Czas wykonania: {}".format(totalTime))

if __name__ == '__main__':
    main()

