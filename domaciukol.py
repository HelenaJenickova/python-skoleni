from math import ceil

class Locality:
    def __init__(self, name: str, locality_coefficient: float):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality: Locality):
        self.locality = locality

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

class Residence(Property):
    def __init__(self, locality: Locality, area: float, commercial: bool):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self) -> int:
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial: 
            tax *= 2
        return ceil(tax)
    
manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

pozemek = Estate(manetin, "land", 900)
dum = Residence(manetin, 120, False)
kancelar = Residence(brno, 90, True)

print(pozemek.calculate_tax())  
print(dum.calculate_tax())     
print(kancelar.calculate_tax()) 

 




