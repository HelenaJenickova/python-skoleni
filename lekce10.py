import json
with open('absolventi.json', encoding='utf-8') as file:
    data = json.load(file)
print(data[-1])

import json
hours = {'po': 8, 'ut': 7, 'st': 6, 'čt': 7, 'pá': 8}
with open('hodiny.json', mode='w', encoding='utf-8') as file:
    json.dump(hours, file, indent=4, ensure_ascii=False)

import json
import requests
result = requests.get("https://api.kodim.cz/python-data/people")
print(result.json())
#nebo data = result.json()
#     print(data[0]["first_name"])

#cviceni 1
import json
import requests
response = requests.get("https://api.kodim.cz/python-data/people", timeout=5)
data = response.json()

print(len(data))
print(data[0].keys())

gender_count = {}
for item in data:
    gender_count[item["gender"]] = gender_count.get(item["gender"], 0) + 1
print(gender_count)

#nebo
import json
import requests 
response = requests.get("https://api.kodim.cz/python-data/people")
data = response.json()
print(len(data))
print(data[0].keys())
gender_count = {}
for person in data:
    gender_count[person['gender']] = gender_count.get(person['gender'], 0) + 1
print(gender_count)


#cvicedni 2 kocky
import json
import requests
response = requests.get("https://catfact.ninja/fact")
data = response.json()

data.pop("length")
with open("kocky.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)

#nebo
response = requests.get("https://catfact.ninja/fact")
cat = response.json()
cat.pop('length')
print(cat)
with open('kocicka.json', mode='w',encoding='utf-8') as file:
    json.dump(cat, file)

import json
with open("zavod.json", encoding="utf-8") as file:
    data = json.load(file)
winner = data[0]
print(winner["jmeno"])
print(data[0]["jmeno"])
winner_time = winner["casy"]["oficialni"]
for runner in data:
    print(runner["jmeno"])

#cviceni zavod zjisti cas zavodnika ktery ziskal stribrnou medaili
import json
with open("zavod.json", encoding="utf-8") as file:
    data = json.load(file)
print(data[1]["casy"]["oficialni"])

#cviceni transformace 
words = {}
with open("words.txt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        first_letter = word[0]
        if first_letter not in words:
            words[first_letter] = [word]
        else:
            words[first_letter].append(word)
for key, value in words.items():
    value = sorted(value)

with open("output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(words, output_file, sort_keys=True, indent=4)
print(words)

#cviceni 2 jinak
words = {}
with open('words.txt', encoding='utf-8') as file:
    for line in file:
        word = line.strip() #odeberu z konce slova whitespace
        first_letter = word[0] #ulozim si prvni pismeno
        if first_letter not in words: #pokud prvni pismeno jeste ve slovniku nemame
            words[first_letter] = [word] #uloz slovo do prazdneho seznamu, klicem bude prvni pismeno
        else: #prvni pismeno ve slovniku mame
            words[first_letter].append(word) #pridej slovo k seznamu ulozenem v prvnim pismenu 
for key in words: #projdi vsechny klice a hodnoty
    words[key] = sorted(words[key]) #serad hodnotu (v nasem pripade seznamy slov)
with open('output.json',encoding='utf-8',mode='w') as output_file:
    json.dump(words, output_file, sort_keys=True, indent = 4) #parametry nastavime razeni a odsazeni

#cviceni dle chatgpt
import json
#vytvorim si prazdny slovnik
slovnik = {}
#otevru vstupni soubor a nacitam ho po radcich
with open("words.txt", "r", encoding="utf-8") as file:
    for radek in file:
        #zbavim se znaku pro novy radek
        slovo = radek.strip()
        #zjistim prvni pisemnko
        if slovo: 
            prvni_pismeno = slovo[0].lower()
        #pokud pismeno neni ve slovniku vytvorim novy klic se seznamem
        if prvni_pismeno not in slovnik:
            slovnik[prvni_pismeno] = [slovo]
        else:
            #jinak slovo pridam do existujiciho seznamu
            slovnik[prvni_pismeno].append(slovo)
#seradim seznamy slov u kazdeho klice
for seznam in slovnik.values():
    seznam.sort()
#zapisu slovnik do json souboru s odsazenim 4 mezery a serazenymi klici
with open("vystup.json", "w", encoding="utf-8") as vystup:
    json.dump(slovnik, vystup, indent=4, sort_keys=True, ensure_ascii=False)





#jinak
import json
def get_time(runner):
    time = runner["casy"]["oficialni"]
    time_split = time.split(":")
    return 
with open("zavod.json", encoding="utf-8") as file:
    data = json.load(file)
sorted(data, key = get_time)
print(data)