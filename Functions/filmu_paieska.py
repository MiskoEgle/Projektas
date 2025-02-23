# Fuctions/filmu_paieska.py

from Classes.filmai import AnimacinisFilmas
from Classes.filmai import DokumentinisFilmas
from Classes.kino_festivalis import KinoFestivalis

def filtruoti_filmus_pagal_tipa(filmai, tipas):
        if tipas == "AnimacinisFilmas":
            return [filmas for filmas in filmai if isinstance(filmas, AnimacinisFilmas)]
        elif tipas == "DokumentinisFilmas":
            return [filmas for filmas in filmai if isinstance(filmas, DokumentinisFilmas)]
        return filmai

def filmu_perziura_ir_paieska():
    festivalis = KinoFestivalis()
    
    while True:
        print("\nFilmų paieška ir peržiūra")
        print("1. Peržiūrėti filmus")
        print("2. Ieškoti filmo")
        print("3. Filtruoti filmus pagal jų tipą")
        
        pasirinkimas = input("Pasirinkite veiksmą: ")
        
        if pasirinkimas == '1':
            
            for filmas in filmai:
                print(f"Pavadinimas: {filmas.pavadinimas}, Trukmė: {filmas.trukme}, Žanras: {filmas.zanras}, Režisierius: {filmas.rezisierius}, Išleidimo metai: {filmas.isleidimo_metai}, Amžiaus reitingas: {filmas.amziaus_reitingas}")
    
        elif pasirinkimas == "2":
            pavadinimas = input("Įveskite filmo pavadinimą (palikite tuščią, jei nenorite ieškoti pagal pavadinimą): ")
            rezisierius = input("Įveskite režisieriaus vardą (palikite tuščią, jei nenorite ieškoti pagal režisierių): ")
            results = festivalis.ieskoti_filmo(pavadinimas if pavadinimas else None, rezisierius if rezisierius else None)
            for filmas in results:
                print(f"Pavadinimas: {filmas.pavadinimas}, Trukmė: {filmas.trukme}, Žanras: {filmas.zanras}, Režisierius: {filmas.rezisierius}, Išleidimo metai: {filmas.isleidimo_metai}, Amžiaus reitingas: {filmas.amziaus_reitingas}")
            
        elif pasirinkimas == '3':
            tipas = input("Įveskite filmo tipą (AnimacinisFilmas arba DokumentinisFilmas): ")
            filmai = festivalis.perziureti_filmus()
            filtruoti = filtruoti_filmus_pagal_tipa(filmai, tipas)
            for filmas in filtruoti:
                print(f"Pavadinimas: {filmas.pavadinimas}, Trukmė: {filmas.trukme}, Žanras: {filmas.zanras}, Režisierius: {filmas.rezisierius}, Išleidimo metai: {filmas.isleidimo_metai}, Amžiaus reitingas: {filmas.amziaus_reitingas}")
        
        elif pasirinkimas == '4':
            print("Išeinama iš programos.")
            break
    
        else:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")