print("Witam w moim podstawowym kalkulatorze kalorii")

waga=int(input("Ile ważysz?"))
wzrost=int(input("Ile masz wzrostu?(w centymetrach)"))
wiek=int(input('Ile masz lat?'))

print("Podaj swoją płeć. Wciśnij 'm' dla mężczyzny lub 'k' dla kobiety. \nDla innyc"
	  "h płci wciśnij literę, z którą się identyfikujesz.")
gender = input()
if gender == "m":
	fx = 5
else:
    fx = -161


cal=(10*waga)+(6.25*wzrost)+(5*wiek)+fx

print("Twoje dzienne zapotrzebowanie na kalorie to:", cal)
