def vynasob(cislo):
    cislo * 10
    print(vynasob (10))

def sum_two_numbers(a,b):
    return a+b
value = sum_two_numbers(2,3)
assert value == 5, "Sum of 2 and 3 should be 5"


def total_price(persons: int, breakfast: int = False) -> int:
    return persons * (850 + 125 * breakfast)
print (total_price(3))
print(total_price(2, True))

def ruleta(vitezne_cislo, rada, sazka):
    if vitezne_cislo == 0:
        return 0
    if vitezne_cislo % 3 == 1 and rada ==1:
        return sazka * 2
    if vitezne_cislo % 3 == 2 and rada == 2:
        return sazka * 2
    if vitezne_cislo % 3 == 3 and rada == 3:  
        return sazka * 2 
    return 0
print (ruleta (0,1,1000))
print(ruleta(1, 1, 1000))
print(ruleta(2, 1, 1000))
print(ruleta(3, 1, 1000))   




def seznam_cisel(numbers, len_max_number, character="."):
    for item in numbers:
        print(f"{character * (len_max_number - len(str(item)))}{item}")

numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# Víme, že největší číslo je současně nejdelší
max_number = max(numbers)
len_max_number = len(str(max_number))
seznam_cisel(numbers, len_max_number)



def seznam(cisla, delka_nejdelsiho, znak="."):
    for item in cisla:
        print(f"{znak * (delka_nejdelsiho - len(str(item)))}{item}")

cisla = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
nejvetsi_cislo = max(cisla)
delka_nejdelsiho = len(str(nejvetsi_cislo))
seznam(cisla, delka_nejdelsiho)


import random


def shuffle_word(word: str) -> str:
    if word.endswith(".") or word.endswith(","):
        interpunction = word[-1]
        word = word[:-1]
    else:
        interpunction = ""
    if len(word) <= 3:
        return f"{word}{interpunction}"
    else:
        shuffled_part = list(word[1:-1])
        random.shuffle(shuffled_part)
        shuffled_part = "".join(shuffled_part)
        return f"{word[0]}{shuffled_part}{word[-1]}{interpunction}"


text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''

for row in text.split("\n"):
    for item in row.split(" "):
        print(shuffle_word(item), end=" ")
    print()

