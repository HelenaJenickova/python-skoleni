#statistika kolikrat byl ktery rod v pozici utocniku
#postup:
#zjistit jake sloupce ma tabulka a jake udaje obsahuje attacker jedna az ctyri ale nekdy prazdne hodnoty
#nacist soubor pomoci with open
#vytvorit slovnik na jmena rodu
#spojit vsechny utocniky do jednoho seznamu a potom zajistit, aby se neobjevovali prazdne hodnoty
# seznam, slovnik s vypisem rodu a nasledne pocitat count techto rodu v jednotlivych pozicich

# Výsledek: Statistika, kolikrát byl který rod v pozici útočníků.
# Postup:
# spojit všechny útočníky do jednoho seznamu a potom zajistit, aby se neobjevovali prázdné hodnoty
#vytvorit slovnik kde bude kazdy rod presne jednou s hodnotou nula
lines = []
with open('battles.tsv', encoding='utf-8') as file:
    for line in file:
        lines.append(line)

#zjitění sloupecku attacker1
column_names = lines[0].split("\t")
index_attacker_1 = column_names.index("attacker_1")
from collections import Counter, defaultdict
result = defaultdict(int)
#vytvori seznam od jednicky[1:], tzn. vynecha nazev attacker_1
for line in lines[1:]:
    line = line.split("\t")
    #cyklus abych nemusela kopirovat attacker1 a pak attacker2 atd udelam cyklus range a z atacker1 umazu 1
    for index in range(index_attacker_1, index_attacker_1 + 4):
    #attacker_1 = line[5].strip()
        attacker = line[index].strip()
        if attacker:
            
   # když je attacker_1 Lenister
    # {"Lannister": 1, "Tully": 8} -> {"Lannister": 2, "Tully": 8}
    # Tohle chceme umeta umi to defaultdict: {"Tully": 8} -> {"Lannister": 1, "Tully": 8}
            result[attacker] += 1
    print(result)

# seznam, slovnik s vypisem rodu a nasledne pocitat count techto rodu v jednotlivých pozicich
#{"Lannister": 10, "Tully: 7"}


#nebo
#pandas python pro datovou analyzu 
lines = []
with open('battles.tsv', encoding='utf-8') as file:
    for line in file:
        lines.append(line)
# Zjištění sloupečku "attacker_1"
column_names = lines[0].split("\t")
index_attacker_1 = column_names.index("attacker_1")
from collections import defaultdict
result = defaultdict(int)
for line in lines[1:]:
    line = line.split("\t")
    for index in range(index_attacker_1, index_attacker_1 + 4):
        attacker = line[index].strip()
        if attacker:
            result[attacker] += 1
print(result)

#nebo kdyz se nam to nechce pocitat
lines = []
with open('battles.tsv', encoding='utf-8') as file:
    for line in file:
        lines.append(line)
# Zjištění sloupečku "attacker_1"
column_names = lines[0].split("\t")
index_attacker_1 = column_names.index("attacker_1")
attackers = []
for line in lines[1:]:
    line = line.split("\t")
    for index in range(index_attacker_1, index_attacker_1 + 4):
        attacker = line[index].strip()
        if attacker:
            attackers.append(attacker)
print(Counter(attackers))

#priklad vytvořit seznam velitelů, kteří zvítězili v boji proti přesile, tj. jejich armáda byla slabší
#  než armáda soupeřů a oni přesto zvítězili. Budeme k tomu potřebovat sloupečky 
# s výsledkem bitvy (attacker_outcome), informacemi o síle útočníků 
# a obránců (attacker_size a defender_size) a se jmény velitelů.
with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()
SL_VYSLEDEK = 13
SL_SILA_UTOCNICI = 17
SL_SILA_OBRANCI = 18
SL_VELITEL_UTOCNICI = 19
SL_VELITEL_OBRANCI = 20
velitele = []
for radek in radky[1:]:
    radek = radek.split("\t")
    #pokud sila utocnici neni prazdna a pokud sila obranci neni prazdna
    if radek[SL_SILA_UTOCNICI] != "" and radek[SL_SILA_OBRANCI] != "":
    #pokud utocnici jsou silnejsi tak si zapisu obrance
        if float(radek[SL_SILA_UTOCNICI]) > float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "loss":
            radek_velitele = radek[SL_VELITEL_OBRANCI].split(", ")
            velitele = velitele + radek_velitele
        if float(radek[SL_SILA_UTOCNICI]) > float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "loss":
            radek_velitele = radek[SL_VELITEL_OBRANCI].split(", ")
            velitele = velitele + radek_velitele
        #utok slabsi nez obrana a vyhrali
        elif float(radek[SL_SILA_UTOCNICI]) < float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "won":
            radek_velitele = radek[SL_VELITEL_UTOCNICI].split(", ")
            velitele = velitele + radek_velitele
        #odstraneni duplikatu je set
print(set(velitele))

#od honzy
with open("python2/python2_0425/battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()
SL_VYSLEDEK = 13
SL_SILA_UTOCNICI = 17
SL_SILA_OBRANCI = 18
SL_VELITEL_UTOCNICI = 19
SL_VELITEL_OBRANCI = 20
velitele = []
for radek in radky[1:]:
    radek = radek.split("\t")
    if radek[SL_SILA_UTOCNICI] != "" and radek[SL_SILA_OBRANCI] != "":
        if float(radek[SL_SILA_UTOCNICI]) > float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "loss":
            radek_velitele = radek[SL_VELITEL_OBRANCI].split(", ")
            velitele = velitele + radek_velitele
        elif float(radek[SL_SILA_UTOCNICI]) < float(radek[SL_SILA_OBRANCI]) and radek[SL_VYSLEDEK] == "win":
            radek_velitele = radek[SL_VELITEL_UTOCNICI].split(", ")
            velitele = velitele + radek_velitele
print(set(velitele))

