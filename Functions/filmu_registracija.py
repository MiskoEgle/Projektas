# Functions/filmu_registracija.py

# import pickle
# from Classes.filmai import Filmai
# from Classes.filmai import AnimacinisFilmas
# from Classes.filmai import DokumentinisFilmas
# from Classes.kino_festivalis import KinoFestivalis

# def filmu_restravimo_meniu():
#     registracija = KinoFestivalis()

#     while True:
#         print("\nFilmu ikelimo Sistema")
#         print("1. Pridėti filmą")
#         print("2. Pašalinti filmą")
#         print("3. Atnaujinti filmą")
#         print("4. Išeiti")

#         pasirinkimas = input("Pasirinkite veiksmą: ")

#         if pasirinkimas == '1':
#             filmo_tipas = input("Kokį filmą norite įvesti? 'anime', 'dokumentinis', 'meninis': ").lower()
#             if filmo_tipas == "anime":
#                 pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
#                 trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
#                 zanras = input("Įveskite filmo žanrą: ").title()
#                 rezisierius = input("Įveskite filmo režisierių: ").title()
#                 isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
#                 amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
#                 animacijos_stilius = input("Įveskite animacijos stiliu: ")
#                 naujas_filmas = AnimacinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, animacijos_stilius)
#                 registracija.issaugoti_duomenis(naujas_filmas)
#             elif filmo_tipas == "dokumentinis":
#                 pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
#                 trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
#                 zanras = input("Įveskite filmo žanrą: ").title()
#                 rezisierius = input("Įveskite filmo režisierių: ").title()
#                 isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
#                 amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
#                 tema = input("Iveskite dokumentinio filmo tema: ")
#                 naujas_filmas = DokumentinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, tema)
#                 registracija.issaugoti_duomenis(naujas_filmas)
#             else:
#                 pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
#                 trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
#                 zanras = input("Įveskite filmo žanrą: ").title()
#                 rezisierius = input("Įveskite filmo režisierių: ").title()
#                 isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
#                 amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
#                 naujas_filmas = Filmai(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas)
#                 registracija.issaugoti_duomenis(naujas_filmas)
#             print("Filmas pridėtas sėkmingai!")

#         elif pasirinkimas == '2':
#             pavadinimas = input("Įveskite filmo pavadinimą, kurį norite pašalinti: ").capitalize()
#             registracija.pasalinti_filma(pavadinimas)
#             print("Filmas pašalintas sėkmingai!")

#         elif pasirinkimas == '3':
#             pavadinimas = input("Įveskite filmo pavadinimą, kurį norite atnaujinti: ").capitalize()
#             atributas = input("Įveskite atributą, kurį norite atnaujinti (pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas): ")
#             nauja_reiksme = input(f"Įveskite naują {atributas}: ")
#             if atributas in ['trukme', 'isleidimo_metai']:
#                 nauja_reiksme = int(nauja_reiksme)
#             atnaujinta = registracija.atnaujinti_filma(pavadinimas, **{atributas: nauja_reiksme})
#             if atnaujinta:
#                 print("Filmas atnaujintas sėkmingai!")
#             else:
#                 print("Filmas nerastas!")

#         elif pasirinkimas == '4':
#             registracija.issaugoti_duomenis()
#             print("Išeinama iš funkcijos.")
#             break

#         else:
#             print("Neteisingas pasirinkimas, bandykite dar kartą.")

# filmu_registracija.py

# import pickle
# from Classes.filmai import Filmai, AnimacinisFilmas, DokumentinisFilmas
# from Classes.kino_festivalis import KinoFestivalis

# def filmu_registravimo_meniu():
#     registracija = KinoFestivalis()

#     while True:
#         print("\nFilmu registravimo Sistema")
#         print("1. Pridėti filmą")
#         print("2. Pašalinti filmą")
#         print("3. Atnaujinti filmą")
#         print("4. Išeiti iš filmu registravimo")

#         pasirinkimas = input("Pasirinkite veiksmą: ")

#         if pasirinkimas == '1':
#             filmo_tipas = input("""Kokį filmą norite įvesti?
#                     1. Animacinis
#                     2. Dokumentinis
#                     3. Meninis: """)
#             if filmo_tipas == "1":
#                 pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
#                 trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
#                 zanras = input("Įveskite filmo žanrą: ").title()
#                 rezisierius = input("Įveskite filmo režisierių: ").title()
#                 isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
#                 amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
#                 animacijos_stilius = input("Įveskite animacijos stilių: ")
#                 naujas_filmas = AnimacinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, animacijos_stilius)
#                 registracija.issaugoti_duomenis(naujas_filmas)
#             elif filmo_tipas == "2":
#                 pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
#                 trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
#                 zanras = input("Įveskite filmo žanrą: ").title()
#                 rezisierius = input("Įveskite filmo režisierių: ").title()
#                 isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
#                 amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
#                 tema = input("Iveskite dokumentinio filmo temą: ")
#                 naujas_filmas = DokumentinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, tema)
#                 registracija.issaugoti_duomenis(naujas_filmas)
#             else:
#                 pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
#                 trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
#                 zanras = input("Įveskite filmo žanrą: ").title()
#                 rezisierius = input("Įveskite filmo režisierių: ").title()
#                 isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
#                 amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
#                 naujas_filmas = Filmai(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas)
#                 registracija.issaugoti_duomenis(naujas_filmas)
#             print("Filmas pridėtas sėkmingai!")

#         elif pasirinkimas == '2':
#             pavadinimas = input("Įveskite filmo pavadinimą, kurį norite pašalinti: ").capitalize()
#             registracija.pasalinti_filma(pavadinimas)
#             print("Filmas pašalintas sėkmingai!")

#         elif pasirinkimas == '3':
#             pavadinimas = input("Įveskite filmo pavadinimą, kurį norite atnaujinti: ").capitalize()
#             atributas = input("Įveskite atributą, kurį norite atnaujinti (pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas): ")
#             nauja_reiksme = input(f"Įveskite naują {atributas}: ")
#             if atributas in ['trukme', 'isleidimo_metai']:
#                 nauja_reiksme = int(nauja_reiksme)
#             atnaujinta = registracija.atnaujinti_filma(pavadinimas, **{atributas: nauja_reiksme})
#             if atnaujinta:
#                 print("Filmas atnaujintas sėkmingai!")
#             else:
#                 print("Filmas nerastas!")

#         elif pasirinkimas == '4':
#             registracija.issaugoti_duomenis()
#             print("Išeinama iš funkcijos.")
#             break

#         else:
#             print("Neteisingas pasirinkimas, bandykite dar kartą.")


# from colorama import Fore, Back, Style, init

# # Inicializuoti colorama (reikalinga Windows sistemose)
# init()

# # Spalvotas tekstas
# print(Fore.RED + 'Raudonas tekstas')
# print(Fore.GREEN + 'Žalias tekstas')
# print(Fore.BLUE + 'Mėlynas tekstas')

# # Spalvotas tekstas su fono spalva
# print(Back.YELLOW + Fore.BLACK + 'Geltonas fonas su juodu tekstu')

# # Atstatyti numatytuosius nustatymus
# print(Style.RESET_ALL + 'Numatytasis tekstas')

# # Fore nurodo teksto spalvą.

# # Back nurodo fono spalvą.

# # Style.RESET_ALL atstatys visus spalvų nustatymus į numatytuosius.


# # Pavyzdys su kino programa:

# # Tarkime, kad turite kino programą ir norite išdėstyti filmų sąrašą su skirtingomis spalvomis:

# # python
# # Copy
# from colorama import Fore, Back, Style, init

# # Inicializuoti colorama
# init()

# # Filmų sąrašas
# films = [
#     {"title": "Inception", "genre": "Sci-Fi"},
#     {"title": "The Shawshank Redemption", "genre": "Drama"},
#     {"title": "The Dark Knight", "genre": "Action"},
#     {"title": "Pulp Fiction", "genre": "Crime"},
# ]

# # Spausdinti filmų sąrašą su skirtingomis spalvomis pagal žanrą
# for film in films:
#     if film["genre"] == "Sci-Fi":
#         print(Fore.CYAN + f"{film['title']} - {film['genre']}")
#     elif film["genre"] == "Drama":
#         print(Fore.GREEN + f"{film['title']} - {film['genre']}")
#     elif film["genre"] == "Action":
#         print(Fore.YELLOW + f"{film['title']} - {film['genre']}")
#     elif film["genre"] == "Crime":
#         print(Fore.RED + f"{film['title']} - {film['genre']}")

# # Atstatyti numatytuosius nustatymus
# print(Style.RESET_ALL)

# # Ši programa išdės filmų sąrašą su skirtingomis spalvomis priklausomai nuo filmo žanro.

# # Kitos alternatyvos:

# # Jei nenorite naudoti colorama, galite naudoti kitas bibliotekas, pvz., termcolor arba tiesiogiai naudoti ANSI spalvų kodus, tačiau colorama yra patogi, nes ji veikia visose operacinėse sistemose (Windows, Linux, macOS).

# # python
# # Copy
# from termcolor import colored

# print(colored('Raudonas tekstas', 'red'))
# print(colored('Žalias tekstas su geltonu fonu', 'green', 'on_yellow'))
# # Šis pavyzdys naudoja termcolor biblioteką, kuri taip pat leidžia lengvai spalvoti tekstą.

# # Tai yra pagrindiniai būdai, kaip galite išdėstyti spalvotas teksto eilutes Python terminale.

# # New chat

from Classes.filmai import Filmai, AnimacinisFilmas, DokumentinisFilmas
from Classes.kino_festivalis import KinoFestivalis

def filmu_registravimo_meniu():
    registracija = KinoFestivalis()

    while True:
        print("\nFilmu registravimo Sistema")
        print("1. Pridėti filmą")
        print("2. Pašalinti filmą")
        print("3. Atnaujinti filmą")
        print("4. Išeiti iš filmu registravimo")

        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == '1':
            filmo_tipas = input("""Kokį filmą norite įvesti?
                    1. Animacinis
                    2. Dokumentinis
                    3. Meninis: """)
            if filmo_tipas == "1":
                pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
                trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
                zanras = input("Įveskite filmo žanrą: ").title()
                rezisierius = input("Įveskite filmo režisierių: ").title()
                isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
                amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
                animacijos_stilius = input("Įveskite animacijos stilių: ")
                naujas_filmas = AnimacinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, animacijos_stilius)
                registracija.prideti_filma(naujas_filmas)
            elif filmo_tipas == "2":
                pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
                trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
                zanras = input("Įveskite filmo žanrą: ").title()
                rezisierius = input("Įveskite filmo režisierių: ").title()
                isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
                amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
                tema = input("Iveskite dokumentinio filmo temą: ")
                naujas_filmas = DokumentinisFilmas(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, tema)
                registracija.prideti_filma(naujas_filmas)
            else:
                pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
                trukme = int(input("Įveskite filmo trukmę (minutėmis): "))
                zanras = input("Įveskite filmo žanrą: ").title()
                rezisierius = input("Įveskite filmo režisierių: ").title()
                isleidimo_metai = int(input("Įveskite filmo išleidimo metus: "))
                amziaus_reitingas = input("Įveskite filmo amžiaus reitingą 'N-8, N-13, N-18': ")
                naujas_filmas = Filmai(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas)
                registracija.prideti_filma(naujas_filmas)
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

