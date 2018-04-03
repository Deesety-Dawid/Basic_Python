import random

a = random.randint(0,100)
print("Witaj w grze zgadywance!\nKomputer losuje liczbę w przedziale 0-100 a ty musisz ją zgadnąć!"
      "('101' do opuszczenia gry)")

while True:
    b = int(input("Wybierz liczbę:"))
    if b == 101:
        break
    elif b < 0 or b > 100:
        print("Wybież liczbę między 0 a 100")
        pass
    else:
        if a > b:
            print("Spróbuj wyżej")
        elif a < b:
            print("Spróbuj niżej")
        else:
            print("Brawo!")
            break
