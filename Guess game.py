import random

a = random.randint(0,100)#losowa liczba importowana z modulu random
b = int(input("Wybierz liczbę:")#liczba podana przez gracza

if a > b:#alternatywy
        print("Spróbuj wyżej")
elif a < b:
        print("Spróbuj niżej")
else:
        print("Brawo!")
