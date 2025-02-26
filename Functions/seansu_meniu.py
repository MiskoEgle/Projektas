from Classes.seansai import SeansuTvarkymas, Seansas
from Classes.kino_festivalis import KinoFestivalis

def seanso_meniu():
    seansu_tvarkymas = SeansuTvarkymas()
    festivalis = KinoFestivalis()

    while True:
        print("\nSeansų Planavimo Sistema")
        print("1. Pridėti seansą")
        print("2. Peržiūrėti seansus")
        print("3. Išeiti")

        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == '1':
            pavadinimas = input("Įveskite filmo pavadinimą: ").capitalize()
            filmas = next((filmas for filmas in festivalis.filmai if filmas.pavadinimas == pavadinimas), None)
            if filmas:
                data = input("Įveskite seanso datą (YYYY-MM-DD): ")
                laikas = input("Įveskite seanso laiką (HH:MM): ")
                vietu_skaicius = int(input("Įveskite vietų skaičių: "))
                naujas_seansas = Seansas(filmas, data, laikas, vietu_skaicius)
                if seansu_tvarkymas.prideti_seansa(naujas_seansas):
                    print("Seansas pridėtas sėkmingai!")
                else:
                    print("Nepavyko pridėti seanso. Patikrinkite, ar tuo metu nėra suplanuota kito filmo.")
            else:
                print("Filmas nerastas!")

        elif pasirinkimas == '2':
            seansai = seansu_tvarkymas.perziureti_seansus()
            for seansas in seansai:
                print(f"Filmas: {seansas.filmas.pavadinimas}, Data: {seansas.data}, Laikas: {seansas.laikas}, Vietų skaičius: {seansas.vietu_skaicius}, Rezervuotos vietos: {seansas.rezervuotos_vietos}")

        elif pasirinkimas == '3':
            seansu_tvarkymas.issaugoti_duomenis()
            print("Išeinama iš programos.")
            break

        else:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")

