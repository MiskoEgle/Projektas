# bilietu_valdymas.py

import Classes.seansai as seansas
import pickle
import os

def issaugoti_duomenis(seansai, failo_pavadinimas):
    with open(failo_pavadinimas, 'wb') as failas:
        pickle.dump(seansai, failas)

def ikelti_duomenis(failo_pavadinimas):
    if os.path.exists(failo_pavadinimas):
        with open(failo_pavadinimas, 'rb') as failas:
            return pickle.load(failas)
    return {}

def bilietai_meniu():
    seansai = ikelti_duomenis('seansai.pkl')
    while True:
        print("1. Rezervuoti vietą")
        print("2. Pirkti bilietą")
        print("3. Atšaukti rezervaciją")
        print("4. Išeiti")
        pasirinkimas = input("Pasirinkite veiksmą: ")
        if pasirinkimas == '1':
            pavadinimas = input("Įveskite seanso pavadinimą: ")
            vietu_skaicius = int(input("Įveskite vietų skaičių: "))
            if pavadinimas not in seansai:
                seansai[pavadinimas] = seansas(pavadinimas)
            try:
                seansai[pavadinimas].rezervuoti_vieta(vietu_skaicius)
                print("Vietos sėkmingai rezervuotos.")
            except ValueError as e:
                print(f"Klaida: {e}")
        elif pasirinkimas == '2':
            pavadinimas = input("Įveskite seanso pavadinimą: ")
            vietu_skaicius = int(input("Įveskite vietų skaičių: "))
            kaina_vienam_bilietui = float(input("Įveskite bilieto kainą: "))
            if pavadinimas not in seansai:
                seansai[pavadinimas] = seansas(pavadinimas)
            try:
                seansai[pavadinimas].pirkti_bilieta(vietu_skaicius, kaina_vienam_bilietui)
                print("Bilietai sėkmingai nupirkti.")
            except ValueError as e:
                print(f"Klaida: {e}")
        elif pasirinkimas == '3':
            pavadinimas = input("Įveskite seanso pavadinimą: ")
            vietu_skaicius = int(input("Įveskite vietų skaičių: "))
            if pavadinimas in seansai:
                try:
                    seansai[pavadinimas].atšaukti_rezervacija(vietu_skaicius)
                    print("Rezervacija sėkmingai atšaukta.")
                except ValueError as e:
                    print(f"Klaida: {e}")
            else:
                print("Seansas nerastas.")
        elif pasirinkimas == '4':
            issaugoti_duomenis(seansai, 'seansai.pkl')
            print("Duomenys išsaugoti. Programa baigia darbą.")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

