from Classes.vietu_rezervacija import Rezervacija, RezervacijuTvarkymas
from Classes.seansai import SeansuTvarkymas

def rezervaciju_meniu():
    rezervaciju_tvarkymas = RezervacijuTvarkymas()
    seansu_tvarkymas = SeansuTvarkymas()

    while True:
        print("\nBilietų Rezervacijos Sistema")
        print("1. Rezervuoti vietas")
        print("2. Peržiūrėti rezervacijas")
        print("3. Peržiūrėti seansus")
        print("4. Išeiti")

        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == '1':
            pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
            seansas = next((seansas for seansas in seansu_tvarkymas.perziureti_seansus() if seansas.filmas.pavadinimas == pavadinimas), None)
            if seansas:
                vartotojas = input("Įveskite savo vardą: ").title()
                vietu_skaicius = int(input("Įveskite vietų skaičių: "))
                nauja_rezervacija = Rezervacija(seansas, vartotojas, vietu_skaicius)
                if rezervaciju_tvarkymas.prideti_rezervacija(nauja_rezervacija):
                    print("Rezervacija pridėta sėkmingai!")
                else:
                    print("Nepavyko pridėti rezervacijos. Patikrinkite, ar yra pakankamai laisvų vietų.")
            else:
                print("Seansas nerastas!")

        elif pasirinkimas == '2':
            rezervacijos = rezervaciju_tvarkymas.uzkrauti_duomenis()
            for rezervacija in rezervacijos:
                print(f"Filmas: {rezervacija.seansas.filmas.pavadinimas}, Data: {rezervacija.seansas.data}, Laikas: {rezervacija.seansas.laikas}, Vartotojas: {rezervacija.vartotojas}, Vietų skaičius: {rezervacija.vietu_skaicius}")

        elif pasirinkimas == '3':
            seansai = seansu_tvarkymas.perziureti_seansus()
            for seansas in seansai:
                print(f"Filmas: {seansas.filmas.pavadinimas}, Data: {seansas.data}, Laikas: {seansas.laikas}, Vietų skaičius: {seansas.vietu_skaicius}, Rezervuotos vietos: {seansas.rezervuotos_vietos}")

        elif pasirinkimas == '4':
            rezervaciju_tvarkymas.issaugoti_duomenis()
            print("Išeinama iš programos.")
            break

        else:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")