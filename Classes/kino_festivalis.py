import pickle

class KinoFestivalis:
    def __init__(self, kelias = 'Data_storage/filmai.pkl'):
        self.failo_pavadinimas = kelias
        self.filmai = self.uzkrauti_duomenis()

    def uzkrauti_duomenis(self):
        try:
            with open(self.failo_pavadinimas, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def issaugoti_duomenis(self):
        with open(self.failo_pavadinimas, 'wb') as file:
            pickle.dump(self.filmai, file)

    def prideti_filma(self, naujas_filmas):
        self.filmai.append(naujas_filmas)
        self.issaugoti_duomenis()
        
    def pasalinti_filma(self, pavadinimas):
        if any(filmas.pavadinimas == pavadinimas for filmas in self.filmai):
            self.filmai = [filmas for filmas in self.filmai if filmas.pavadinimas != pavadinimas]
            self.issaugoti_duomenis()
            return print("Filmas pašalintas sėkmingai!")
        return print("Filmas nerastas!")

        
    def atnaujinti_filma(self, pavadinimas, **kwargs):
        for filmas in self.filmai:
            if filmas.pavadinimas == pavadinimas:
                for key, value in kwargs.items():
                    setattr(filmas, key, value)
                self.issaugoti_duomenis()
                return True
        return False

    def perziureti_filmus(self):
        for filmas in self.filmai:
                print(f"Pavadinimas: {filmas.pavadinimas}, Trukmė: {filmas.trukme}, Žanras: {filmas.zanras}, Režisierius: {filmas.rezisierius}, Išleidimo metai: {filmas.isleidimo_metai}, Amžiaus reitingas: {filmas.amziaus_reitingas}")
        return 

    def ieskoti_filmo(self, pavadinimas=None, rezisierius=None):
        results = self.filmai
        if pavadinimas:
            results = [filmas for filmas in results if filmas.pavadinimas == pavadinimas]
        if rezisierius:
            results = [filmas for filmas in results if filmas.rezisierius == rezisierius]
        return results 
