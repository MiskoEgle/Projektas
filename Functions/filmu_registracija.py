# Functions/filmu_registracija.py


# from colorama import Fore, Back, Style, init

# # Inicializuoti colorama 
# init()

# # Spalvotas tekstas
# print(Fore.RED + 'Raudonas tekstas')
# print(Fore.GREEN + 'Žalias tekstas')
# print(Fore.BLUE + 'Mėlynas tekstas')

# # Spalvotas tekstas su fono spalva




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

