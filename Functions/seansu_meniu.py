# seansu_meniu.py



# from Classes.seansai import SeansuPlanavimas

# def seanso_meniu():
#     while True:
#         print("\nSeanso planavimas")
#         print("1. Pridėti seansą")
#         print("2. Rodyti seansus")
#         print("3. Išeiti iš seanso planavimo")
        
#         pasirinkimas = input("Pasirinkite veiksmą: ")
        
#         if pasirinkimas == '1':
#             filmo_pavadinimas = input("Įveskite filmo pavadinimą: ")
#             data_laikas = input("Įveskite seanso datą ir laiką (YYYY-MM-DD HH:MM): ")
#             SeansuPlanavimas.prideti_seansa(filmo_pavadinimas, data_laikas)
        
#         elif pasirinkimas == '2':
#            SeansuPlanavimas.rodyti_seansus()
        
#         elif pasirinkimas == '3':
#             print("\nIšėjome iš seanso planavimo")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Bandykite dar kartą.")


import Classes.seansai as planavimas

def seanso_meniu():
    
    while True:
        print("\nSeanso planavimas")
        print("1. Pridėti seansą")
        print("2. Rodyti seansus")
        print("3. Išeiti iš seanso planavimo")
        
        pasirinkimas = input("Pasirinkite veiksmą: ")
        
        if pasirinkimas == '1':
            planavimas.prideti_seansa()
        
        elif pasirinkimas == '2':
           planavimas.rodyti_seansus()
        
        elif pasirinkimas == '3':
            print("\nIšėjome iš seanso planavimo")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
