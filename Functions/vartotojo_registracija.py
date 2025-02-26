from Classes.vartotojai import Organizatoriai, Sveciai
import config as config
import os
import pickle
import re

kelias = os.path.join("Data_storage", "vartotojai.pkl")

def validuoti_slaptazodi(slaptazodis):
    if len(slaptazodis) < 8:
        print("Slaptažodis turi būti ilgesnis kaip 7 simboliai")
        return False
    if not re.search("[a-z]", slaptazodis):
        print("Slaptaždyje turi būti bent viena mažoji raidė")
        return False
    if not re.search("[A-Z]", slaptazodis):
        print("Slaptaždyje turi būti bent viena didžioji raidė")
        return False
    if not re.search("[0-9]", slaptazodis):
        print("Slaptaždyje turi būti bent vienas skaičius")
        return False
    return True
       
def registruoti_vartotoja(vartotojai, vardas, pavarde, role=None, slaptazodis=None):
    try:
        if role == "organizatorius":
            if not validuoti_slaptazodi(slaptazodis):
                raise ValueError("Slaptazodis neatitinka reikalavimu")
            vartotojas = Organizatoriai(vardas, pavarde, role, slaptazodis)
            vartotojai["organizatoriai"].append(vartotojas)
        else:
            vartotojas = Sveciai(vardas, pavarde, role)
            vartotojai["sveciai"].append(vartotojas)
        with open(kelias, "wb") as failas:
            pickle.dump(vartotojai, failas)
    except Exception as e:
        print(f"Klaida: {e}")

def prisijungti(vartotojai, vardas, pavarde, slaptazodis=None):
    try:
        for organizatorius in vartotojai["organizatoriai"]:
            if organizatorius.vardas == vardas and organizatorius.pavarde == pavarde:
                if organizatorius.slaptazodis == slaptazodis:
                    print("\nPrisijungta kaip organizatorius\n")
                    config.organizatoriu_meniu()
                else:
                    raise ValueError("Neteisingas slaptazodis")
        for svecias in vartotojai["sveciai"]:
            if svecias.vardas == vardas and svecias.pavarde == pavarde:
                print("\nPrisijungta kaip svecias\n")
                config.svecio_meniu()
        raise ValueError("Tokio vartotojo nėra")
    except Exception as e:
        print(f"Klaida: {e}")

def ikelti_vartotojus():
    try:
        with open(kelias, "rb") as f:
            return pickle.load(f)
    except:
        return  {"organizatoriai": [], "sveciai": []}

vartotojai = ikelti_vartotojus()

def vartotojo_meniu():
    while True:
        pasirinkimas = input("""Pasirinkite veiksma:
            1 - Registracija
            2 - Prisijungimas
            3 - Iseiti iš programos:  """)
        if pasirinkimas == "1":
            vardas = input("Iveskite varda: ").capitalize()
            pavarde = input("Iveskite pavarde: ").capitalize()
            ivestis = input("""Ar esate organizatorius?
                        1. Taip
                        2. Ne:  """)
            if ivestis == "1":
                role = "organizatorius"
                while True:
                    slaptazodis = input("Sukurkite slaptazodi: ")
                    if validuoti_slaptazodi(slaptazodis):
                        break
                    else:
                        print("Slaptazodis neatitinka reikalavimu. Bandykite dar karta.")
                registruoti_vartotoja(vartotojai, vardas, pavarde, role, slaptazodis)
            else:
                role = "svecias"
                registruoti_vartotoja(vartotojai, vardas, pavarde, role)
                
        elif pasirinkimas == "2":
            vardas = input("Iveskite varda: ").capitalize()
            pavarde = input("Iveskite pavarde: ").capitalize()
            role = input("""Ar esate organizatorius?
                        1. Taip
                        2. Ne:  """)
            if role == "1":
                slaptazodis = input("Iveskite slaptazodi: ")
                print(prisijungti(vartotojai, vardas, pavarde, slaptazodis))
            else:
                print(prisijungti(vartotojai, vardas, pavarde))
                
        elif pasirinkimas == "3":
            print("Išeinu iš programos")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar karta.")
            