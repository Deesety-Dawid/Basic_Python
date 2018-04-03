print("Kalkulator lokatowy")
stan = float(input("Jaki masz początkowy stan konta?: " ))
procent = float(input("Jakie jest oprocentowanie lokaty? (sama liczba)?: "))
czas = int(input("Na ile lat jest ta lokata?: "))

wynik = stan * ((1+(procent/100/12))**(12*czas))

print("Przy stanie początkowym {:.2f}zł w czasie {} lat powinieneś mieć na swojej "
      "lokacie {:.2f}zł" .format(stan, czas, wynik))
