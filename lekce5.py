
class Contact:
    def __init__(self, name, position):
        self.name = name
        self.position = position
class Employee(Contact):
    def __init__(self, name, position, holiday_entitlement):
        # name = parametr metody __init__
        # self.name = atribut třídy (atribut objektů)
        super().__init__(name, position)
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement = self.holiday_entitlement - days
            return "Užij si to"
        else:
            return f"Máš nárok jen na {self.holiday_entitlement} dní."
    def __str__(self):
        vypis = f"{self.name} pracuje na pozici {self.position}."
        return vypis
    
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        # Tady použijeme metodu __init__ třídy Employee
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car
    def __str__(self):
        vypis_employee = super().__str__()
        return  f"{vypis_employee} má {self.subordinates} podřízených"
marian = Manager("Marian Přísný", "manažer", 25, 2, "skoda octavia")
print(marian.take_holiday(10))
print(marian)



#priklad 1 Cenny balik
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

package = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
valuable_package = ValuablePackage("Pernerova 702/39, Praha", 12.47, "nedoručen", 5000)
print(package)
print(valuable_package)
print(valuable_package.delivery_price())

#cviceni2 Cena prepravy
print(package.delivery_price())
print(valuable_package.delivery_price())


#cviceni 3 Jizdenky
class Ticket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

class TrainTicket(Ticket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class
    
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price
        elif self.fare_class == "business":
            return self.basic_price * 1.3
        else:
            return self.basic_price

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages
    
    def get_price(self):
        if self.fare_class == "economy":
            base_price = self.basic_price
        else:
            base_price = self.basic_price * 1.5
        
        return base_price + (self.checkout_luggages * 2000)


train_economy = TrainTicket(150, "A12", "economy")
train_business = TrainTicket(150, "B05", "business")

print(f"Cena vlakové jízdenky economy: {train_economy.get_price()} Kč")
print(f"Cena vlakové jízdenky business: {train_business.get_price()} Kč")

plane_economy = PlaneTicket(6000, "15C", "economy", 1)
plane_business = PlaneTicket(6000, "3A", "business", 1)

print(f"Cena letenky economy s jedním zavazadlem: {plane_economy.get_price()} Kč")
print(f"Cena letenky business s jedním zavazadlem: {plane_business.get_price()} Kč")

#cviceni 4 audioknihy
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

item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)

total_time = item_1.get_time_to_read() + item_2.get_time_to_read()
print(total_time)



#Datové třídy

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    position: str
    holiday_entitlement: int = 25

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."

frantisek = Employee("František Novák", "konstruktér")
print(frantisek.take_holiday(5))
print(frantisek.take_holiday(15))
print(frantisek.take_holiday(10))

#cviceni na datove tridy Streamovaci sluzba
from dataclasses import dataclass
@dataclass
class Movie:
    title: str
    genre: str
    runtime: int
    def __str__(self):
        return f"{self.title} spadá do žánru {self.genre} a trvá {self.runtime} minut."
    def get_runtime(self):
        return self.runtime
@dataclass
class Series:
    title: str
    genre: str
    episode_count: int
    episode_runtime: int
    def __str__(self):
        return f"{self.title} spadá do žánru {self.genre} má {self.episode_count} epizod a trvá {self.episode_runtime}."
    def get_runtime(self):
        return self.episode_count * self.episode_runtime
@dataclass
class User:
    user_name: str
    total_time: int = 0
    def record_time(self, time):
        self.total_time = self.total_time + time
film = Movie("Jak utopit doktora Mráčka", "komedie", 120)
serial = Series("Pohotovost", "scifi", 60, 60)
helena = User("Helena")

print(film)
print(serial)

delka_film = film.get_runtime()
helena.record_time(delka_film)
delka_serial = serial.get_runtime()
helena.record_time(delka_serial)
print(helena.total_time)




#cviceni bonusove
from dataclasses import dataclass
@dataclass
class Movie():
    title: str
    genre: str
    runtime: int
    def __str__(self):
        return f'nazev: {self.title}, zanr: {self.genre}, delka: {self.runtime}'
    def get_runtime(self):
        self.runtime
@dataclass
class Series():
    title: str
    genre: str
    episode_count: int
    episode_runtime: int
    def __str__(self):
        return f'nazev: {self.title}, zanr: {self.genre}, pocet epizod: {self.episode_count}, delka epizody: {self.episode_runtime}'
    def get_runtime(self):
        return self.episode_count * self.episode_runtime
@dataclass
class User():
    user_name: str
    total_time: int = 0



#
class Movie:
    def __init__(self, title: str, genre: str, runtime: int):
        self.title = title
        self.genre = genre
        self.runtime = runtime
    def __str__(self) -> str:
        return f"Film: {self.title} | Žánr: {self.genre} | Délka: {self.runtime} minut"

class Series:
    def __init__(self, title: str, genre: str, episode_count: int, episode_runtime: int):
        self.title = title
        self.genre = genre
        self.episode_count = episode_count
        self.episode_runtime = episode_runtime
    def __str__(self) -> str:
        return (f"Seriál: {self.title} | Žánr: {self.genre} | "
                f"Počet epizod: {self.episode_count} | Délka jedné epizody: {self.episode_runtime} minut")
# Vytvoření jednoho filmu a jednoho seriálu
film = Movie("Amélie z Montmartru", "romantická komedie", 122)
serial = Series("Černobyl", "historické drama", 5, 60)
# Výpis
print(film)
print(serial)





