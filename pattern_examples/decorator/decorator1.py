#!/usr/bin/env python3.4

# Towrzymy funkcję
def my_function(value):
    print("To ja, Twoja funkcja. Dostałam", value)
    
# Wywołanie funkcji to...
my_function("coś")

# Tworzymy funkcję przyjmującą... funkcję
# i uruchamiającą ją..
def runner(function, *args, **kwargs):
    print("W funkcji runner(), uruchamiam przekazaną funkcję...")
    function(*args, **kwargs)

# Uruchamiamy funckcję przyjmującą funkcję

runner(my_function, "inne coś")
