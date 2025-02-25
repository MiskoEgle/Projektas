# reitingai.py

import pickle
import os

class FilmuReitingavimas:
    def __init__(self, failas_filmai='Data_storage/filmai.pkl', failas_reitingai='Data_storage/reitingai.pkl'):
        self.failas_filmai = failas_filmai
        self.failas_reitingai = failas_reitingai
        self.filmai = self.uzkrauti_filmus()
        self.reitingai = self.uzkrauti_reitingus()
        
    def uzkrauti_filmus(self):
        filmai = []
        if os.path.exists(self.failas_filmai):
            with open(self.failas_filmai, 'rb') as f:
                filmai = pickle.load(f)
        return filmai

    def uzkrauti_reitingus(self):
        reitingai = []
        if os.path.exists(self.failas_reitingai):
            with open(self.failas_reitingai, 'rb') as f:
                reitingai = pickle.load(f)
        return reitingai
    
    def issaugoti_duomenis(self):
        with open(self.failas_reitingai, 'wb') as f:
            pickle.dump(self.reitingai, f)

    def isaugoti_filma(self):
        with open(self.failas_filmai, 'wb') as f:
            pickle.dump(self.filmai, f)

    def filmo_reitingavimas(self, vartotojas, filmas, reitingas):
        if filmas not in self.filmai:
            print("Filmas nerastas.")
            return
        if vartotojas in self.reitingai.get(filmas, {}):
            print("Jūs jau įvertinote šį filmą.")
            return
        if filmas not in self.reitingai:
            self.reitingai[filmas] = {}

        self.reitingai.append(vartotojas, filmas, reitingas)
        self.issaugoti_duomenis()
        self.vidutinis_filmo_ivertinimas(filmas)
        print(f"Filmas '{filmas}' įvertintas {reitingas} balais.")

    def vidutinis_filmo_ivertinimas(self, filmas):
        reitingas = self.reitingai.get(filmas, {}).values()
        if reitingas:
            vidutinis_ivertinimas = sum(reitingas) / len(reitingas)
            self.filmai[reitingas] = vidutinis_ivertinimas
            self.isaugoti_filma()
            print(f"Vidutinis filmo '{filmas}' įvertinimas atnaujintas: {vidutinis_ivertinimas:.2f}")

    # def filmu_saraso_atvaizdavimas(self, pavadinimas):
        # if pavadinimas:
            
        # for filmas in self.reitingai:
        #     if filmas for filmas:
        #         for reitingas in self.filmai:
        #             print(f"Filmas: {filmas}, Vidutinis įvertinimas: {reitingas}")

