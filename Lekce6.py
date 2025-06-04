class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def get_info(self)
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.holiday_entitlement = holiday_entitlement
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
# Volám metodu __str__() mateřské třídy a k výsledku přidávám další řetězec
        return super().__str__() + f" Má {self.subordinates} podřízených."

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2, "Škoda Octavia")
print(marian)


#isinstance() 
if isinstance(marian, Manager):
    print("objekt pochází ze třídy Manager (nebo jejích potomků).")
else:
    print("objekt nepochází ze třídy Manager (nebo jejích potomků).")

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee("František Novák", "konstruktér", 25)
employee_list = [marian, marketa, frantisek]

expected_people = 0
for employee in employee_list:
    if isinstance(employee, Manager):
       print(f"Pozvánka pro {employee.name} na školení leadershipu.")  
       expected_people = expected_people + 1

print(f"Čekáme {expected_people} osob.")      

#hasattr()
class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car): 
        # Volám metodu __init__() mateřské třídy
        super().__init__(name, position, holiday_entitlement)
        self.holiday_entitlement = holiday_entitlement
        self.car = car

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee("František Novák", "konstruktér", 25)
jakub = Salesman("Jakub Čmelák", "business development manager", 25, "Škoda Octavia Scout")
employee_list = [marian, marketa, frantisek, jakub]

for item in employee_list:
    if hasattr(item, "car"):
        print(item.car)

#getattr()
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
atribut = input("jaky atribut mam vypsat?")
auto = getattr(marian, "car", "neznámé auto")
print(auto)

frantisek = Employee("František Novák", "konstruktér", 25)
auto = getattr(frantisek, "car", "Nemá auto")
print(auto)


#příklad 1 Celková hodnota balíků
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
        elif self.weight < 20:
            return 159
        else:
            return 359
class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value
    def __str__(self):
        return f"{super().__str__()} Jeho hodnota je {self.value}."
    def delivery_price(self):
        return super().delivery_price() + self.value * 0.05
package_0 = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
valuable_package = ValuablePackage("Pernerova 702/39, Praha", 12.47, "nedoručen", 5000)
print(package_0)
print(valuable_package)
print(valuable_package.delivery_price())
print(package_0.delivery_price())
print(valuable_package.delivery_price())
#zadání z příkladu dědičnosti
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]
#1
total_value = 0
for package in package_list:
    if hasattr(package, "value"):
        total_value += package.value
print(f"celkova hodnota cennych baliku v aute je {total_value} Kč.")
#2
total_value_alternative = 0
for package in package_list:
    if isinstance(package, ValuablePackage):
        total_value_alternative += package.value
print(f"celkova hodnota cennych baliku v aute pomoci funkce isinstance je {total_value_alternative} Kč.")
#3
total_value_getattr = 0
for package in package_list:
    package_value = getattr(package, "value", 0)
    total_value_getattr += package_value
print(f"celkova hodnota cennych baliku v aute pomoci getattr je {total_value_getattr}")

#zjisteni zda balik byl dorucen a tak neni v aute pro zjisteni hodnoty
#1
for package in package_list:
    if hasattr(package, "value") and package.state == "nedoručen":
        total_value += package.value
print(f"celkova hodnota cennych baliku v aute je {total_value} Kč.")    
#2
total_value_alt = 0
for package in package_list:
    if isinstance(package, ValuablePackage) and package.state == "nedoručen":
        total_value_alt += package.value
print(f"Celková hodnota cenných balíků v autě (pomocí isinstance) je {total_value_alt} Kč.")
#3
tal_value_getattr = 0
for package in package_list:
    if package.state == "nedoručen":
        package_value = getattr(package, 'value', 0)
        total_value_getattr += package_value
print(f"Celková hodnota cenných balíků v autě (pomocí getattr) je {total_value_getattr} Kč.")

#cvičení Vypravěči
class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def get_time_to_read(self):
        pass    
class Book(Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages
    def get_info(self):
        return f"Kniha '{self.title}' má {self.pages} stran a stojí {self.price} Kč."
    def get_time_to_read(self):
        return self.pages * 4 / 60
class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator
    def get_time_to_read(self):
        return self.duration_in_hours
#řešení chci vyplsat jen ty kde je oblibeny autor 
favourite_narrator = "Zbyšek Horák"

item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)
item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

all_items = [item_1, item_2, item_3]

for item in all_items:
    print(item.title) #vyjede mi vsechny tituly knizek


for item in all_items:
    if isinstance(item, AudioBook) and item.narrator == favourite_narrator:
        print(item.title)

for item in all_items:
    if hasattr(item, "narrator") and item.narrator == favourite_narrator:
        total_value += package.value
        print(item.title)

for item in all_items:
    if getattr(item, "narrator", None) == favourite_narrator:
        print(item.title)

#Abstraktní třídy
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_circ():
        pass

    @abstractmethod
    def get_area():
        pass

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def get_circ(self):
        return 4 * self.a

    def get_area(self):
        return self.a * self.a
    
small_square = Square(10)
print(small_square.get_circ())

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_circ(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b
large_rectangle = Rectangle(20, 25)
total_area = small_square.get_area() + large_rectangle.get_area()
print(f"Celková plocha obou obrazců je {total_area}.")

# pro testovani falesny kod

from abc import ABC, abstractmethod

class OurClient(ABC):
    @abstractmethod
    def send_request(self, data):
        pass

class HttpClient(OurClient):
    def send_request(self, data):
        print("sending real request")

class FakeClient(OurClient):
    def send_request(self, data):
        print("pretending to send request")

HttpClient().send_request(data="example data")