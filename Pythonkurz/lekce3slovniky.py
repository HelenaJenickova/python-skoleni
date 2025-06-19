item_list = ["Čajová konvička s hrnky", 899, True]
# Jak získat ze seznamu hodnotu "Čajová konvička s hrnky"
print(item_list[0])
item = {"title": "Čajová konvička s hrnky",
        "price": 899, "in_stock": True}
#Pridavam novou hodnotu 
item["weight"]=1.2
#a upravuji existujiho hodnotu
#ulozim si klic do promenne
key = "price"
#zapisu hodnotu
item["key"]=939
#prectu hodnotu
print(item[key])

print(f"Vybraná položka {item["title"]} je a {item["price"]} stojí Kč.")

if "weight" in item:
    print(item["weight"])
else:
    print("Hmotnost není zadaná.")


item = {"title": "Čajová konvička s hrnky",
        "price": 899,
        "in_stock": True}
key = input("Co tě zajímá: ")
print(item[key])

#1.priklad Vysvedceni
vysvedceni = {"cestina": 2,
              "matika": 1,
               "dejepis": 3 }
print(vysvedceni)

#2.priklad Detektivky
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
sales["Noc, která mě zabila"]= 0
sales["Vrah zavolá v deset"]= sales["Vrah zavolá v deset"] + 100
print(sales)
    
#3.priklad Tombola
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
key = int(input("Číslo tvého lístu:"))
if key in tombola:
    print(f"Vyhráváš {tombola[key]}")
else:
    print("Bohužel nevyhráváš nic.")

#4.priklad Paranoidnivecirek
passwords = {"Jiří": "tajne-heslo", 
             "Natálie": "jeste-tajnejsi-heslo", 
             "Klára": "nejtajnejsi-heslo"}

key = input("Zadej jméno: ")
if key in passwords:
    password = input("Zadej heslo: ")
    if password == passwords[key]:
        print("Smíš vstoupit.")
    else:
        print("Toto není správné heslo.")
else:
    print("Bohužel nejsi na seznamu.")

#5.priklad
sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
print(len(sausages))
sausages["Naty"] = 0
print(len(sausages))
sausages.pop("Naty")

#slovníky a cykly
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
total_sales = 0
for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
#nebo:
for p1, p2 in sales.items():
    print(f"Knihy{p1}bylo prodáno{p2}výtisků.")
    total_sales = total_sales + value
print(total_sales)
print(f"Celkem bylo prodáno {total_sales} výtisků.")

#nebo
total_sales = sum(sales.values())
print(total_sales)

#Dvourozměrné tabulky
#slovník pro jednu knihu:
book = {"title": "Zkus mě chytit",
        "sold": 4165,
        "price": 347,
        "year": 2018}
#seznam - má hranaté závorky uvnitř je slovník
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total_sales = 0
for item in books: 
   # vypis nazvy knih: print(item["title"]) 
   #rozmysli si, jestli spustit následující řádek, je třeba
   #zkontrolovat, že knížka vyšla v roce 2019
   if item["year"] == 2019:
        total_sales= total_sales + item["sold"] * item["price"]
print(total_sales)

#1.cvičení Vysvědčení 2
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}
import statistics
avg = statistics.mean(school_report.values())
print(statistics.mean(school_report.values()))

#prumerne_znamky = avg(school_report.values())
#print(prumerne_znamky)

print("Predmety, ze kterých student získal známku výborně: ")
for key, value in school_report.items():
    if value == 1:
        print(key)

#nebo
soucet = sum(school_report.values()) 
pocet = len(school_report)
prumer = soucet/pocet
print(prumer) 

for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)

#2.cvičení Čtenářský deník
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
pocet_stran = 0
dobre_knihy = 0
for book in books:
    pocet_stran = pocet_stran + book['pages']
    if book['rating'] >= 8:
        dobre_knihy = dobre_knihy + 1
print(pocet_stran)
print(dobre_knihy)

#nebo
page_count = 0
favourite_books = 0
for item in books:
    page_count = page_count + item["pages"]
    if item["rating"] >= 8:
        favourite_books = favourite_books + 1

print(f"Gustal celkem přečetl {page_count} knih.")
print(f"Počet knih s hodnocením alespoň 8: {favourite_books}.")

#nebo
pocet_stran = 0
for key in books:
    pocet_stran = pocet_stran + key["pages"]
print(f"Gustal celkem přečetl {pocet_stran} knih.")

oblibene_knihy = 0
for key in books:
    if key["rating"] >= 8:
        oblibene_knihy = oblibene_knihy + 1
print(f"Počet knih s hodnocením alespoň 8: {oblibene_knihy}.")

#3.cviceni Poznavaci znacky
plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

for key, value in plates.items():
    if key[1] == "P":
        print(value)

#4.cvičení Recepty kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
recept = {
        'nazev': 'Batáty se šalvějí a pancettou',
        'narocnost': 'stredni',
        'doba': 30,
        'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
} 
import math
celkova_cena = 0
for vec in recept["ingredience"]:
    cena = vec[-1]
    cena = float(cena.split()[0])
    celkova_cena +=  cena
print(f"Cena jídla je KČ {math.ceil(celkova_cena)}")




