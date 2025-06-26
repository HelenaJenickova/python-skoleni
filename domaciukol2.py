import json
import requests

ico = input("zadej ico:")
url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
results = requests.get("url")
data = results.json()
obchodni_jmeno = data.get("obchodniJmeno", "Neznámé jméno")
adresa = data.get("sidlo", {}).get("textovaAdresa", "Neznámá adresa")
print(obchodni_jmeno)
print(adresa)

nazev = input("\nZadej název subjektu, který chceš vyhledat: ")
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = {"obchodniJmeno": nazev}
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",
    headers=headers,json=data)
if response.status_code == 200:
    vysledky = response.json()
    subjekty = vysledky.get("ekonomickeSubjekty", [])
    pocet = vysledky.get("pocetCelkem", 0)

    print(f"\nNalezeno subjektů: {pocet}")

    for subjekt in subjekty:
        jmeno = subjekt.get("obchodniJmeno", "Neznámé jméno")
        ico = subjekt.get("ico", "Neznámé IČO")
        print(f"{jmeno}, {ico}")
else:
    print("Nepodařilo se provést vyhledávání.")