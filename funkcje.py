def kategorie_miast(miasto):
    Duze_Miasta = ["Warszawa", "Kraków", "Gdańsk", "Wrocław"]
    if miasto in Duze_Miasta:
        return "duże miasto"
    elif len(miasto) > 8:
        return "średnie miasto"
    else:
        return "małe miasto"

print(kategorie_miast("Pcim"))