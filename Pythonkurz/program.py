venecky = [1, 2, 4, 1, 6, 0, 1]
print(venecky[5])
venecky [5] = 12
print(venecky[0])
print(venecky[5])
print(venecky[2:5])
print(venecky[:3])
print(venecky[3:])

venecky = [1, 2, 4, 1, 6, 0, 1]
#chci od pozice 0 do pozice 5 ale cislo na pozici 5 uy tam nebude
#0:5 = 0,1,2,3,4
venecky_vsedni_den = venecky [0:5]
print(venecky_vsedni_den)
venecky_vikend = venecky[5:7]
print(venecky_vikend)
#-2 je předposlední a -1 poslední

#chci delku seznamu
venecky = [1, 2, 4, 1, 6, 0, 1]
delka_seznamu = len(venecky)
print(delka_seznamu)
print(len(venecky))
#soucet venecku
soucet_venecku = sum(venecky)
minimalni_cislo = min(venecky)
print(minimalni_cislo)
maximalni_cislo = max(venecky)
print(maximalni_cislo)
print(venecky[2:5])
print(venecky[:3])
print(venecky[3:])

venecky = [1, 2, 4, 1, 6, 0, 1]
serazeny_seznam = sorted(venecky, reverse=True)
print(serazeny_seznam)

jmeno = "Helena"
print(jmeno[:3])
print(len(jmeno))

inzerat = "Na této pracovní pozici budete využívat PyTHon a SQL"
inzerat = inzerat.lower()
if "Python" in inzerat:
    print("Je to pro mě!")
else: 
    print ("není tam python")

   
pohyby = [1200, -250, -800, 540, 721, -613, -222]
print(pohyby [2])
print(pohyby [2:])
print(len(pohyby))
print(min(pohyby), max(pohyby))
print(sum(pohyby))

# 2 průměr
seznam = [1,2,3,4,5]
print(sum(seznam)/len(seznam))

# 3 rozpětí rozdíl mezi min a max hodnotou
seznam = [1,2,3,4,5]
print(max(seznam)-min(seznam))

# 5 střed seznamu
s = [1,2,3,4,5]
print(s[len(s)//2])

# 6 střed senamu podruhé¨
s = [1, 2, 3, 4, 5, 6, 7, 8]

if len(s) % 2 == 0:
    prostredni_cislo = s[len(s) // 2 - 1]
    print(prostredni_cislo) # tato varianta se vytiskne pokud je pocet prvku v seznamu sudy
else:
    prostredni_cislo = s[len(s) // 2]
    print(prostredni_cislo) # tato varianta se vytiskne pokud je pocet prvku v seznamu lichy

# 4 zasedačka
akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]
pohovory = 0
jazyky = []
for radek in akce:
    if "pohovor" in radek:
        pohovory = pohovory + 1
        if "jazykový kurz" in radek:
            jazyk = radek.replace("jazykovy kurz - ", "")
            if jazyk not in jazyky:
                jazyky.apppend(jazyk)
print(f"Pohovorů: {pohovory}.")
jazyky = ", ".join(jazyky)
print(f"Jazyky: {jazyky}.") 




retezec = "Ahoj   "
retezec = retezec.lower()
# retezec_mala_pismena = retezec.lower()
retezec = retezec.strip()
print(retezec)

dny = "pondělí;čtvrtek;pátek"
# dny = ["pondělí", "čtvrtek"]
dny = dny.split(";")
pocet_dnu = len(dny)
print(pocet_dnu)

#join()
temata = ["metody", "funkce", "slicing"]
# "Témata kurzu: metody, funkce, slicing"
# metody, funkce, slicing
# Pomocí ", " mi spoj (join) seznam temata
temata_retezec = ", ".join(temata)
print(f"Témata kurzu jsou: {temata_retezec}")

#replace
text = "Kurz vede lektor Marek"
novy_text = text.replace("Marek", "Martin")
# Vypíše Kurz vede lektor Martin
print(novy_text)

#append
guest_list = ["Jirka", "Klára", "Natálie"]
# Vypíše Natálie
print(guest_list[-1])
guest_list.append("Adéla")
# Vypíše Adéla
print(guest_list[-1])

jen_cisla = "10"
print(jen_cisla.isdecimal())

jmeno = 'Helena'
print('Helena'.upper())
print('Helena'.lower())
# cisla jako text
hodnoty = ['12', '1', '7', '-11']


akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]

pohovory = 0
jazyky = []
for radek in akce:
    if "pohovor" in radek:
        pohovory = pohovory + 1
    if "jazykový kurz" in radek:
        jazyk = radek.replace("jazykový kurz - ", "")
        if jazyk not in jazyky:
            jazyky.append(jazyk)

jazyky = ",".join(jazyky)
print(f"bylo pohovorů: {pohovory}")

print(f"Jazyky: {jazyky}.")

#čísla jako text
hodnoty = ['12', '1', '7', '-11']
treti_cislo = hodnoty[2]
treti_cislo = int(treti_cislo)
vysledek = treti_cislo + 4
vysledek = str(vysledek)
hodnoty[2] = vysledek
print(hodnoty)

hodnotyy = '12.1 1.68 7.45 -11.51'



