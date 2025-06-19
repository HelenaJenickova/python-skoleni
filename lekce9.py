lines = []
with open("mereni.txt", encoding="utf-8") as file:
    for line in file:
        line = line.split()
        line[1] = float(line[1])
        lines.append(line)
print(lines)

#priklad vyplata
llines = []
vykazy = []
with open("vykaz.txt", encoding="utf-8") as file:
    for lline in file:
        vykazy.append(float(lline))
hodinova_mzda = int(input("napis hodinovou mzdu v kč:"))
celkova_mzda = 0
for vykaz in vykazy:
    celkova_mzda += hodinova_mzda * vykaz
print(celkova_mzda)
print(celkova_mzda/len(vykazy))

#nebo
vykaz = []
with open("vykaz.txt") as file:
    for line in file:
        vykaz.append(int(line))
print(vykaz)
mzda = input("zadejte mzdu:")
celkemhodin = 0
for mesic in vykaz:
    celkemhodin = celkemhodin + mesic
print(f"vyplata za rok je {celkemhodin * mzda}")


#priklad kryptomeny
krypto = []
with open("transaction_list.csv") as file:
    for line in file:
        krypto.append(line.strip().split(";"))
print(krypto)
celkova_hodnota = 0
for zaznam in krypto:
    celkova_hodnota = celkova_hodnota + float(zaznam[1])
print(celkova_hodnota)

#zápis do souboru

text_1 = "toto je můj zápis do souboru.\n"
text_2 = "dalsi kousek textu"
with open("soubor.txt", mode="w", encoding="utf-8") as file:
    #print(text, file = file)
    file.write(text_1)
    file.write(text_2)

names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
with open('uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        #print(name, file=output_file)
        file.write(f"{name}\n")

#cviceni zapis do souboru 
#dny v mesici
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
with open("kalendar.txt", encoding="utf-8", mode="w") as soubor:
    for dny in pocty_dni:
        #print(dny, file=soubor)
        soubor.write(f"{dny}\n")

#vytvoření souboru
nazevsouboru = input("Zadej název souboru: ")
text = input("Zadej text: ")
with open(nazevsouboru, mode="w", encoding="utf-8") as file:
    print(text, file=file)

#rozepsaná výplata
vyplata_po_mesicich = []
hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))
with open('vykaz.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        vyplata = float(radek) * hodinova_mzda
        vyplata_po_mesicich.append(vyplata)
        print(vyplata)
with open("vyplata_po_mesicich.txt", "w", encoding="utf-8") as soubor:
    for hodnota in vyplata_po_mesicich:
        print(hodnota, file=soubor)

#druha_verze
lines = []
vykazy = []

with open('vykaz.txt', encoding='utf-8') as file:
    for line in file:
        vykazy.append(float(line))

hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))

with open("vyplata.txt", "w", encoding="utf-8") as soubor:
    for vykaz in vykazy:
        mzda_za_mesic = hodinova_mzda * vykaz
        print(mzda_za_mesic, file=soubor)



