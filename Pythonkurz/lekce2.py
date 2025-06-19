import math
import statistics 
from statistics import mean
cislo = 2.2
math.ceil(cislo)
math.floor(cislo)
print(math.ceil(cislo))
print(math.floor(cislo))

seznamcisel = [3, 8, 12, 19]
prumer = statistics.mean(seznamcisel)
print(prumer)

def privitani():
    print("ahoj")
privitani()

def podekuj():
    print("dekuji")
podekuj()

def privitani(language_code):
    if language_code == "cs":
        print ("ahoj")
    elif language_code == "de":
        print("Hallo")
    else:
        print("Hello")
privitani("de")
privitani("cs")

def soucet(a, b):
    return a + b
result = soucet(5, 15)
print(result)

def convert_to_czk(euro):
    exchange_rate = 26
    return euro * exchange_rate
result = convert_to_czk(2)
print(result)

#Násobení
def mult(a, b):
    return a * b
result = mult(3, 5)
print(result)

pepa = 'pepa je dobrej'
print(pepa)

# Funkce pro převody jednotek Délka
# 🔹 Kilometry ↔️ Míle
# kilometry_na_mile(km): mile = km * 0.621371
def kilometry_na_mile(kilometry):
    return kilometry * 0.621371

def mile_na_kilometry(mile):
    return mile/0.6

print(kilometry_na_mile(10))
print(mile_na_kilometry(10))
#mile na km namorni mile
def mile_na_kilometry(mile, namorni=False):
    if not namorni:
        return mile * 1.609344
    else:
        return mile * 1.852
londonoxfordkm = mile_na_kilometry(59.7)
print(londonoxfordkm)

belfast_new_york = mile_na_kilometry(2758.13, True)
print(belfast_new_york)



def mile_na_kilometry(mile: float, namorni: bool = False) -> float:
    if not namorni:
        return mile * 1.609344
    else:
        return mile * 1.852
belfast_new_york = mile_na_kilometry(2758.13, True)
print(belfast_new_york)


promenna = False
if not promenna: # nebo if promenna == false:
    print("promenna je vyhodnocena jako nepravda")

promennna = ""
if not promennna:
    print("promenna je nepravda nebo prazdna hodnota")





# 🔹 Metry ↔️ Stopy
# metry_na_stopy(m): stopy = m * 3.28084
# 🔹 Centimetry ↔️ Palce
# centimetry_na_palec(cm): palce = cm / 2.54
# ⚖️ Hmotnost
# 🔹 Kilogramy ↔️ Libry
# kilogramy_na_libry(kg): libry = kg * 2.20462
# 🧴 Objem
# 🔹 Litry ↔️ Galony (americké)
# litry_na_galony(l): galony = l * 0.264172
# 🚗 Rychlost
# 🔹 Kilometry/hod ↔️ Míle/hod
# kmh_na_mph(kmh): mph = kmh * 0.621371
# 🌡️ Teplota
# 🔹 Celsia ↔️ Fahrenheit
# celsia_na_fahrenheit(c): f = (c × 9/5) + 32
def celsius_na_fahrenheit(c):
  return (c * 9 / 5) + 32
# fahrenheit_na_celsia(f): c = (f − 32) × 5/9



#mesic narozeni
def mesic_narozeni(rodnecislo: str) -> int:
    month = int(rodnecislo[2:4]) 
    return month % 50
# 10%50 je 10 a 60%50 je taky 10
print(mesic_narozeni("9207054439"))
print(mesic_narozeni ("9555125899"))

def mesicnarozeni(rodnecislo):
    result = int(rodnecislo[2:4])
    if result > 50:
        result = result - 50
    return result
print(mesic_narozeni("9207054439"))
print(mesic_narozeni ("9555125899"))

#rámeček
#Zadej slovo: ahoj
#********
#* ahoj *
#********
#ahoj má délku 4 a rámeček má délku 2+4+2
#rámeček má délku: 2+délka slova +2
def ramecek(slovo:str):
    delka_horniho_radku = len(slovo) + 4
    print(delka_horniho_radku * "*")
    print(f"* {slovo} * ")
    print(delka_horniho_radku * "*")
ramecek("czechitas")


def frame(word, character = "*"):
    print(character * (len(word) * 4))
    print(f"{character} {word} {character}")
    print(character * (len(word) + 4))


def vynasob(cislo):
    return cislo * 10
print(vynasob (10))

def spocitejcenu(cenazakus, kusy, postovne):
    cena = cenazakus * kusy + postovne
    print(cena)
spocitejcenu(250, 3, 90)

def spocitejcenu2(cenazakus, kusy, postovne):
    cena1 = cenazakus * kusy + postovne
    return cena1
print(spocitejcenu2(250, 3, 90))

def vypocitej_slevu(kod):
    if kod == "mamradajavu":
        return 5
    elif kod == "mamradapython":
        return 30
    else:
        return 0

def kofein_za_den(pocet_espresso, pocet_filtrovana=0):
    return pocet_espresso * 75 + pocet_filtrovana * 150
kofein_za_den(2,1)







