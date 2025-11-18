wiek = int(input("Podaj swój wiek: "))

if wiek < 15:
    print("Jesteś dzieckiem")
elif wiek < 18:
    print("Jesteś niepełnoletni")
elif wiek == 18:
    print("Masz dokładnie 18 lat")
elif wiek <= 60:
    print("Jesteś pełnoletni")
else:
    print("Jesteś stary")
