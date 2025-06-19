lines = [
    "2904,č",
    "7390,0",
    "6950;8",
    "3300,4",
    "10570,8",
    "1310,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    line = line.split(",")
    try:
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    except Exception:
        print("Data jsou chybná")
        print(line)

print(avg_sales)

#cviceni 1 Knihy

knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]
try:
    index = input("Zadej index knihy: ")
    index = int(index)
    print(knihy[index])
except Exception:
    print("neco je spatne a ja jsem lina ti rict co")
    

#cviceni 2 knizni serie

knihy = {
    "1984": [328],
    "Pán Prstenů": [423, 352, 416],
    "Hornblower": [256, 352, 288, 304],
    "Problém tří těles": [400, 512, 608]
}
try:
    nazev = input("Zadej název knižní série: ")
    if nazev not in knihy:
        print("tato kniha tam neni")
    else:
        stranek_za_den = int(input("Kolik stran přečteš každý den? "))
        stranek_celkem = sum(knihy[nazev])
        pocet_dni = stranek_celkem / stranek_za_den
        pocet_dni = round(pocet_dni)
        print(f"Celou sérii přečteš za {pocet_dni} dní.")
except Exception:
    print("neco je spatne")