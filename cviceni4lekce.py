class Car:
    def __init__(self, spz, brand_model, km):
        self.spz = spz
        self.brand_model = brand_model
        self.km = km
        self.available = True  # Na začátku je auto volné

    def __str__(self):
        return f"Značka: {self.spz} typ vozidla: {self.brand_model}"
    
    def rent_car(self):
        if self.available:
            self.available = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def return_car(self, new_km, days_used):
        if not self.available:
            self.km = new_km
            self.available = True
            if days_used < 8:
                price = 400 * days_used
            else:
                price = 300 * days_used
            return f"Auto bylo vráceno. Cena za půjčení je {price} Kč."
        return "vozidlo jiz je vraceno"

# Vytvoření objektů aut
car1 = Car("4A2 3020", "Peugeot 403 Cabrio", 47534)
car2 = Car("1P3 4747", "Škoda Octavia", 41253)


znacka = input("Jakou značku si přejete půjčit? (Peugeot / Škoda): ").strip().lower()

if znacka == "peugeot":
    print(car1)
    print(car1.rent_car())
    rented_car = car1
elif znacka == "škoda" or znacka == "skoda":
    print(car2)
    print(car2.rent_car())
    rented_car = car2
else:
    print("Tuto značku nemáme v nabídce.")
    exit()

# Pokus o další půjčení téhož auta
print("\nDruhý pokus o půjčení stejného auta:")
if znacka == "peugeot":
    print(car1)
    print(car1.rent_car())
elif znacka == "škoda" or znacka == "skoda":
    print(car2)
    print(car2.rent_car())

# Dotaz na vrácení auta
print("\nVrácení vozidla")
nove_km = int(input("Zadejte stav tachometru při vrácení: "))
dny = int(input("Zadejte počet dní, po které jste auto používali: "))

print(rented_car.return_car(nove_km, dny))
print(rented_car)





class Employee:
    def __init__(self, name, position, holiday_entitlement, probation_period):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.probation_period = probation_period

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement = self.holiday_entitlement - days
            return "Užij si to"
        else:
            return f"Máš nárok jen na {self.holiday_entitlement} dní."
        
    def __str__(self):
        if self.probation_period:
            period_string = "Je ve zkušební době"
        else:
            period_string = "Není ve zkušební době"
        return f"{self.name} pracuje na pozici {self.position}. {period_string}"
    

frantisek = Employee("František Novák", "konstruktér", 25, True)
klara = Employee("Klára Nová", "konstruktérka", 25, False)
print(frantisek)
print(klara)





class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
        
    def delivery_price(self):
        if self.weight < 10:
            return 129
        if self.weight < 20:
            return 159
        return 359
    
    def deliver(self):
        if self.state == "nedoručen":
            self.state = "doručen"
            return f"Balík odevzdán na adrese {self.address}."
        return f"Balík již byl doručen na adresu {self.address}."


package_1 = Package("Grimmauldovo náměstí 11", 15, "nedoručen")
package_2 = Package("Godrikův důl 47", 3, "nedoručen")
package_3 = Package("Vydrník svatého Drába 13", 20, "nedoručen")
package_list = [package_1, package_2, package_3]

total_weight = 0
total_price = 0

for item in package_list:
    total_weight += item.weight
    total_price += item.delivery_price()

print(f"Celková váhe je: {total_weight} Celková cena: {total_price}")




class Car:
    def __init__(self, registracni_znacka, znacka_a_typ_vozidla, najete_kilometry, volne=True):
        self.registracni_znacka = registracni_znacka
        self.znacka_a_typ_vozidla = znacka_a_typ_vozidla
        self.najete_kilometry = najete_kilometry
        self.volne = volne

   # def __str__(self):
    #    return f"Registrační značka: {self.registracni_znacka} Typ vozidla: {self.znacka_a_typ_vozidla}"

    def rent_car(self):
        if self.volne:
            self.volne = False
            return "Potvrzuji zapůjčení vozidla"
        return "Vozidlo není k dispozici"

    def return_car(self, stav_tachometru, pocet_dni):
        if not self.volne:
            self.najete_kilometry = stav_tachometru
            self.volne = True
            if pocet_dni < 8:
                cena = 400 * pocet_dni
            else:
                cena = 300 * pocet_dni
            return f"Vozidlo vráceno, cena za pronájem: {cena} CZK"
        return "Vozidlo je již vráceno"

peugeot = Car("4A2 3020", "Peugeot 403 Cabrio",47534)
skoda = Car("1P3 4747", "Škoda Octavia", 41253)

car_list = [peugeot, skoda]
rented_car = None

znacka_vozu = input("Zvolte typ vozidla, k dispozici Škoda nebo Peugeot: ")

if znacka_vozu in ["Škoda", "Peugeot"]:
    for item in car_list:
        if znacka_vozu in item.znacka_a_typ_vozidla:
            print(item.rent_car())
            rented_car = item
else:
    print("Tato značka není k dispozici")
    exit()

# Pokus o další půjčení téhož auta
print("\nDruhý pokus o půjčení stejného auta:")
if znacka_vozu == "peugeot":
    print(peugeot)
    print(peugeot.rent_car())
elif znacka_vozu == "škoda" or znacka_vozu == "skoda":
    print(skoda)
    print(skoda.rent_car())

# Dotaz na vrácení auta
print("\nVrácení vozidla")
stav_tachometru = int(input("Zadejte stav tachometru při vrácení: "))
pocet_dni = int(input("Zadejte počet dní, po které jste auto používali: "))

if rented_car:
    print(rented_car.return_car(stav_tachometru, pocet_dni))
print(rented_car)
