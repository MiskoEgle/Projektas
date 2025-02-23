# Classes/filmai.py

class Filmai:
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas):
        self.pavadinimas = pavadinimas
        self.trukme = trukme
        self.zanras = zanras
        self.rezisierius = rezisierius
        self.isleidimo_metai = isleidimo_metai
        self.amziaus_reitingas = amziaus_reitingas

    def __repr__(self):
        return f"Filmas({self.pavadinimas}, {self.trukme}, {self.zanras}, {self.rezisierius}, {self.isleidimo_metai}, {self.amziaus_reitingas})"

class AnimacinisFilmas(Filmai):
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas, animacijos_stilius):
        super().__init__(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas)
        self.animacijos_stilius = animacijos_stilius

class DokumentinisFilmas(Filmai):
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas, tema):
        super().__init__(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas)
        self.tema = tema
