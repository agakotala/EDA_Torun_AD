#definiujemy funkcję o nazwie kategorie_miast, która przyjmuje jeden argument: miasto
def kategorie_miast(miasto):
    #tworzymy listę dużych miast, które chcemy traktować jako "duże"
    Duze_Miasta = ["Warszawa", "Kraków", "Gdańsk", "Wrocław"]

    #sprawdzamy, czy podane miasto znajduje się na liście dużych miast
    if miasto in Duze_Miasta:
        return "duże miasto"         # eśli tak — zwracamy kategorię "duże miasto"

    #jeśli nie jest dużym miastem, sprawdzamy, czy jego nazwa jest długa (więcej niż 8 znaków)
    elif len(miasto) > 8:
        return "średnie miasto"      #jeśli nazwa jest dłuższa — traktujemy je jako "średnie"

    else:
        return "małe miasto"         #jeżeli nie spełnia żadnego z powyższych warunków — jest "małe"

#wywołujemy funkcję z argumentem "Pcim" i drukujemy wynik
print(kategorie_miast("Pcim"))
