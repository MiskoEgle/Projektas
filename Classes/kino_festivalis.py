# Classes/kino_festivalis.py

import pickle

class KinoFestivalis:
    def __init__(self, kelias = 'Data_storage/filmai.pkl'):
        self.failo_pavadinimas = kelias
        self.filmai = self.uzkrauti_duomenis()

    def uzkrauti_duomenis(self):
        try:
            with open(self.failo_pavadinimas, 'rb') as failas:
                return pickle.load(failas)
        except (FileNotFoundError, EOFError):
            return []

    def issaugoti_duomenis(self):
        with open(self.failo_pavadinimas, 'wb') as failas:
            pickle.dump(self.filmai, failas)

    def prideti_filma(self, naujas_filmas):
        self.filmai.append(naujas_filmas)
        self.issaugoti_duomenis()
        
    def pasalinti_filma(self, pavadinimas):
        self.filmai = [filmas for filmas in self.filmai if filmas.pavadinimas != pavadinimas]
        self.issaugoti_duomenis()
        
    def atnaujinti_filma(self, pavadinimas, **kwargs):
        for filmas in self.filmai:
            if filmas.pavadinimas == pavadinimas:
                for key, value in kwargs.items():
                    setattr(filmas, key, value)
                self.issaugoti_duomenis()
                return True
        return False

    def perziureti_filmus(self):
        return self.filmai

    def ieskoti_filmo(self, pavadinimas=None, rezisierius=None):
        results = self.filmai
        if pavadinimas:
            results = [filmas for filmas in results if filmas.pavadinimas == pavadinimas]
        if rezisierius:
            results = [filmas for filmas in results if filmas.rezisierius == rezisierius]
        return results
