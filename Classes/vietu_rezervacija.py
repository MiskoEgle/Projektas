
import pickle
class Rezervacija:
    def __init__(self, seansas, vartotojas, vietu_skaicius):
        self.seansas = seansas
        self.vartotojas = vartotojas
        self.vietu_skaicius = vietu_skaicius

class RezervacijuTvarkymas:
    def __init__(self, duomenys='Data_storage/bilietai.pkl'):
        self.bilietu_failas = duomenys
        self.rezervacijos = self.uzkrauti_duomenis()

    def uzkrauti_duomenis(self):
        try:
            with open(self.bilietu_failas, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def prideti_rezervacija(self, rezervacija):
        if rezervacija.seansas.vietu_skaicius - rezervacija.seansas.rezervuotos_vietos >= rezervacija.vietu_skaicius:
            rezervacija.seansas.rezervuotos_vietos += rezervacija.vietu_skaicius
            self.rezervacijos.append(rezervacija)
            self.issaugoti_duomenis()
            return True
        return False

    def issaugoti_duomenis(self):
        with open(self.bilietu_failas, 'wb') as file:
            pickle.dump(self.rezervacijos, file)