# seansai.py

# class Seansas:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.vietos = 120
#         self.rezervuotos_vietos = 0
#         self.pajamos = 0.0

#     def rezervuoti_vieta(self, vietu_skaicius):
#         if vietu_skaicius <= 0:
#             raise ValueError("Vietų skaičius turi būti teigiamas.")
#         if self.rezervuotos_vietos + vietu_skaicius > self.vietos:
#             raise ValueError("Nepakanka laisvų vietų.")
#         self.rezervuotos_vietos += vietu_skaicius

#     def pirkti_bilieta(self, vietu_skaicius, kaina_vienam_bilietui):
#         self.rezervuoti_vieta(vietu_skaicius)
#         self.pajamos += vietu_skaicius * kaina_vienam_bilietui

#     def atšaukti_rezervacija(self, vietu_skaicius):
#         if vietu_skaicius <= 0 or vietu_skaicius > self.rezervuotos_vietos:
#             raise ValueError("Netinkamas vietų skaičius atšaukimui.")
#         self.rezervuotos_vietos -= vietu_skaicius


# import pickle
# import os
# from datetime import datetime

# class SeansuPlanavimas():
#     def __init__(self, duomenys='Data_storage/seansai.pkl'):
#         self.failas_seansai = duomenys
#         self.seansai = self.duomenu_uzkrovimas()

#     def duomenu_uzkrovimas(self):
#         if os.path.exists(self.failas_seansai):
#             with open(self.failas_seansai, 'rb') as file:
#                 return pickle.load(file)
#         return {}

#     def issaugoti_duomenis(self):
#         with open(self.failas_seansai, 'wb') as file:
#             pickle.dump(self.seansai, file)

#     # Papildomas funkcionalumas, kuris užtikrina ne daugiau kaip 2-jų filmų peržiūrą per dieną 
#     def prideti_seansa(self, data_laikas, filmo_pavadinimas):
#         try:
#             filmo_pavadinimas = input("Įveskite filmo pavadinimą: ")
#             datos_ivestis = input("Įveskite seanso datą ir laiką (YYYY-MM-DD HH:MM): ")
            
#             data_laikas = datetime.strptime(datos_ivestis, '%Y-%m-%d %H:%M')
#             data = data_laikas.date()
#             seansu_skaicius = sum(1 for dt in self.seansai if dt.date() == data)
            
#             if seansu_skaicius >= 2:
#                 raise ValueError("Šiai dienai jau suplanuoti du filmai.")
#             if data_laikas in self.seansai:
#                 raise ValueError("Šiuo metu jau yra suplanuotas kitas filmas.")
            
#             self.seansai[data_laikas] = filmo_pavadinimas
#             self.issaugoti_duomenis()
#             print("Seansas sėkmingai pridėtas.")
#         except ValueError as e:
#             print(f"Klaida: {e}")
#         except Exception as e:
#             print(f"Nenumatyta klaida: {e}")

#     def rodyti_seansus(self):
#         if not self.seansai:
#             print("Nėra suplanuotų seansų.")
#         else:
#             for data_laikas, filmo_pavadinimas in sorted(self.seansai.items()):
#                 print(f"{data_laikas}: {filmo_pavadinimas}")
        

import pickle
import os
from datetime import datetime

class SeansuPlanavimas():
    def __init__(self, duomenys='Data_storage/seansai.pkl'):
        self.failas_seansai = duomenys
        self.seansai = self.duomenu_uzkrovimas()

    def duomenu_uzkrovimas(self):
        if os.path.exists(self.failas_seansai):
            with open(self.failas_seansai, 'rb') as file:
                return pickle.load(file)
        return {}

    def issaugoti_duomenis(self):
        with open(self.failas_seansai, 'wb') as file:
            pickle.dump(self.seansai, file)

    # Papildomas funkcionalumas, kuris užtikrina ne daugiau kaip 2-jų filmų peržiūrą per dieną 
    def prideti_seansa(self, data_laikas, filmo_pavadinimas):
        try:
            filmo_pavadinimas = input("Įveskite filmo pavadinimą: ")
            datos_ivestis = input("Įveskite seanso datą ir laiką (YYYY-MM-DD HH:MM): ")
            
            data_laikas = datetime.strptime(datos_ivestis, '%Y-%m-%d %H:%M')
            data = data_laikas.date()
            seansu_skaicius = sum(1 for dt in self.seansai if dt.date() == data)
            
            if seansu_skaicius >= 2:
                raise ValueError("Šiai dienai jau suplanuoti du filmai.")
            if data_laikas in self.seansai:
                raise ValueError("Šiuo metu jau yra suplanuotas kitas filmas.")
            
            self.seansai[data_laikas] = filmo_pavadinimas
            self.issaugoti_duomenis()
            print("Seansas sėkmingai pridėtas.")
        except ValueError as e:
            print(f"Klaida: {e}")
        except Exception as e:
            print(f"Nenumatyta klaida: {e}")

    def rodyti_seansus(self):
        if not self.seansai:
            print("Nėra suplanuotų seansų.")
        else:
            for data_laikas, filmo_pavadinimas in sorted(self.seansai.items()):
                print(f"{data_laikas}: {filmo_pavadinimas}")
        
