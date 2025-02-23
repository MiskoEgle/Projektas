# Functions/filmu_registracija.py

import pickle
from Classes.filmai import Filmai
from Classes.filmai import AnimacinisFilmas
from Classes.filmai import DokumentinisFilmas
from Classes.kino_festivalis import KinoFestivalis

def filmu_restravimo_meniu():
    registracija = KinoFestivalis()

    while True:
        print("\nFilmu ikelimo Sistema")
        print("1. Pridėti filmą")
        print("2. Pašalinti filmą")
        print("3. Atnaujinti filmą")
        print("4. Išeiti")

        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == '1':
            filmo_tipas = input("Kokį filmą norite įvesti? 'anime', 'dokumentinis', 'meninis': ").lower()
            if filmo_tipas == "anime":
                pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
                trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
                zanras = input("Įveskite filmo žanrą: ").title()
                rezisierius = input("Įveskite filmo režisierių: ").title()
                isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
                amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
                animacijos_stilius = input("Įveskite animacijos stiliu: ")
                naujas_filmas = AnimacinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, animacijos_stilius)
                registracija.issaugoti_duomenis(naujas_filmas)
            elif filmo_tipas == "dokumentinis":
                pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
                trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
                zanras = input("Įveskite filmo žanrą: ").title()
                rezisierius = input("Įveskite filmo režisierių: ").title()
                isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
                amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
                tema = input("Iveskite dokumentinio filmo tema: ")
                naujas_filmas = DokumentinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, tema)
                registracija.issaugoti_duomenis(naujas_filmas)
            else:
                pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
                trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
                zanras = input("Įveskite filmo žanrą: ").title()
                rezisierius = input("Įveskite filmo režisierių: ").title()
                isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
                amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
                naujas_filmas = Filmai(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas)
                registracija.issaugoti_duomenis(naujas_filmas)
            print("Filmas pridėtas sėkmingai!")

        elif pasirinkimas == '2':
            pavadinimas = input("Įveskite filmo pavadinimą, kurį norite pašalinti: ").capitalize()
            registracija.pasalinti_filma(pavadinimas)
            print("Filmas pašalintas sėkmingai!")

        elif pasirinkimas == '3':
            pavadinimas = input("Įveskite filmo pavadinimą, kurį norite atnaujinti: ").capitalize()
            atributas = input("Įveskite atributą, kurį norite atnaujinti (pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas): ")
            nauja_reiksme = input(f"Įveskite naują {atributas}: ")
            if atributas in ['trukme', 'isleidimo_metai']:
                nauja_reiksme = int(nauja_reiksme)
            atnaujinta = registracija.atnaujinti_filma(pavadinimas, **{atributas: nauja_reiksme})
            if atnaujinta:
                print("Filmas atnaujintas sėkmingai!")
            else:
                print("Filmas nerastas!")

        elif pasirinkimas == '4':
            registracija.issaugoti_duomenis()
            print("Išeinama iš funkcijos.")
            break

        else:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")

