# filmu_reitingavimas.py

from Classes.reitingai import FilmuReitingavimas
from Classes.vartotojai import Sveciai

def filmu_reitingavimas():
    system = FilmuReitingavimas()
    
    while True:
        print("\n1. Rodyti filmų sąrašą")
        print("2. Reitinguoti filmą")
        print("3. Išeiti")
        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == '1':
            system.filmu_saraso_atvaizdavimas()
        elif pasirinkimas == '2':
            vartotojas = Sveciai("Jonas", "Jonaitis", "svecias")
            filmas = input("Įveskite filmo pavadinimą: ")
            reitingas = int(input("Įveskite įvertinimą (1-10): "))
            system.filmo_reitingavimas(vartotojas, filmas, reitingas)
        elif pasirinkimas == '3':
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
