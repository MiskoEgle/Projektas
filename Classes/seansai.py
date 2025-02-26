import pickle
     
class Seansas:
    def __init__(self, filmas, data, laikas, vietu_skaicius):
        self.filmas = filmas
        self.data = data
        self.laikas = laikas
        self.vietu_skaicius = vietu_skaicius
        self.rezervuotos_vietos = 0

    def __repr__(self):
        return f"Seansas({self.filmas.pavadinimas}, {self.data}, {self.laikas}, {self.vietu_skaicius})"

class SeansuTvarkymas:
    def __init__(self, duomenys='Data_storage/seansai.pkl'):
        self.failas_seansai = duomenys
        self.seansai = self.uzkrauti_duomenis()

    def uzkrauti_duomenis(self):
        try:
            with open(self.failas_seansai, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def prideti_seansa(self, seansas):
        if not self.ar_laikas_uzimtas(seansas.data, seansas.laikas):
            self.seansai.append(seansas)
            self.issaugoti_duomenis()
            return True
        return False

    def ar_laikas_uzimtas(self, data, laikas):
        for seansas in self.seansai:
            if seansas.data == data and seansas.laikas == laikas:
                return True
        return False

    def perziureti_seansus(self):
        return self.seansai

    def issaugoti_duomenis(self):
        with open(self.failas_seansai, 'wb') as file:
            pickle.dump(self.seansai, file)