# Functions/vartotoju_registracija.py

import os
import pickle
import re
from Classes.vartotojai import Organizatoriai
from Classes.vartotojai import Sveciai

kelias = os.path.join("Data_storage", "vartotojai.pkl")

def validuoti_slaptazodi(slaptazodis):
    if len(slaptazodis) < 8:
        return False
    if not re.search("[a-z]", slaptazodis):
        return False
    if not re.search("[A-Z]", slaptazodis):
        return False
    if not re.search("[0-9]", slaptazodis):
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
        with open(kelias, "wb") as f:
            pickle.dump(vartotojai, f)
    except Exception as e:
        print(f"Klaida: {e}")

def prisijungti(vartotojai, vardas, pavarde, slaptazodis=None):
    try:
        for organizatorius in vartotojai["organizatoriai"]:
            if organizatorius.vardas == vardas and organizatorius.pavarde == pavarde:
                if organizatorius.slaptazodis == slaptazodis:
                    return "Prisijungta kaip organizatorius"
                else:
                    raise ValueError("Neteisingas slaptazodis")
        for svecias in vartotojai["sveciai"]:
            if svecias.vardas == vardas and svecias.pavarde == pavarde:
                return "Prisijungta kaip svecias"
        raise ValueError("Tokio vartotojo nėra")
    except Exception as e:
        print(f"Klaida: {e}")

def ikelti_vartotojus():
    try:
        with open(kelias, "rb") as f:
            vartotojai = pickle.load(f)
    except FileNotFoundError:
        vartotojai = {"organizatoriai": [], "sveciai": []}
    return vartotojai

vartotojai = ikelti_vartotojus()

def vartotojo_meniu():
    
    while True:
        pasirinkimas = input("Pasirinkite veiksma: 1 - Registracija, 2 - Prisijungimas, 3 - Iseiti: ")
        if pasirinkimas == "1":
            vardas = input("Iveskite varda: ")
            pavarde = input("Iveskite pavarde: ")
            role = input("Ar esate organizatorius? (taip/ne): ").lower()
            if role == "taip":
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
            vardas = input("Iveskite varda: ")
            pavarde = input("Iveskite pavarde: ")
            role = input("Ar esate organizatorius? (taip/ne): ").lower()
            if role == "taip":
                slaptazodis = input("Iveskite slaptazodi: ")
                print(prisijungti(vartotojai, vardas, pavarde, slaptazodis))
            else:
                print(prisijungti(vartotojai, vardas, pavarde))
        elif pasirinkimas == "3":
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar karta.")
       

