from math import ceil
from abc import ABC, abstractmethod

class Locality:
    def __init__(self, name: str, locality_coefficient: float):
        self.name = name
        self.locality_coefficient = locality_coefficient

    def __str__(self):
        return f"{self.name} má koeficient {self.locality_coefficient}"
    
class Property(ABC):
    def __init__(self, locality: Locality):
        self.locality = locality
    @abstractmethod
    def calculate_tax(self) -> int:
        pass 

class Estate(Property):
    
    estate_type_coefficients = {"land": 0.85, "building_site": 9, "forrest": 0.35, "garden": 2}    

    def __init__(self, locality: Locality, estate_type: str, area: float):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

#dan je plocha(area) * typ pozemku (estate_type) * místní koeficient(locality_coefficient)
    def calculate_tax(self) -> int:
        coeff = self.estate_type_coefficients[self.estate_type]
        tax = self.area * coeff * self.locality.locality_coefficient
        return ceil(tax)
    
    def __str__(self):
        typy = {"land":"zemedelsky_pozemek", "building_site":"stavebni_pozemek", "forrest":"lesni_pozemek", "garden":"zahrada"}
        return f"{typy[self.estate_type]}, v lokalitě {self.locality} má {self.area}m ctverecnich a dan je {self.calculate_tax()}Kč."

class Residence(Property):
    def __init__(self, locality: Locality, area: float, commercial: bool):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self) -> int:
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial: 
            tax = tax * 2
        return ceil(tax)
    
    def __str__(self):
        typ = "komerční objekt" if self.commercial else "rezidenční objekt"
        return f"{typ} v {self.locality} má {self.area}m ctverecnich a dan je {self.calculate_tax()}Kč."
    
class TaxReport:
    def __init__(self, name: str, property_list: list[Property]):
        self.name = name
        self.property_list = property_list

    def add_property(self, prop: Property):
        self.property_list.append(prop)

    def calculate_total_tax(self) -> int:
        total = 0
        for prop in self.property_list:
            total = total + prop.calculate_tax()
        return total

    def __str__(self):
        output = f"Daňové přiznání {self.name}\n"
        for prop in self.property_list:
            output += str(prop) + "\n"
        output = f"\nCelková daň: {self.calculate_total_tax()} Kč"
        return output
    
manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

pozemek = Estate(manetin, "land", 900)
dum = Residence(manetin, 120, False)
kancelar = Residence(brno, 90, True)

print(pozemek.calculate_tax())  
print(dum.calculate_tax())     
print(kancelar.calculate_tax()) 

 




