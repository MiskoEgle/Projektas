class Filmai:
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, reitingas = 0):
        self.pavadinimas = pavadinimas
        self.trukme = trukme
        self.zanras = zanras
        self.rezisierius = rezisierius
        self.isleidimo_metai = isleidimo_metai
        self.amziaus_reitingas = amziaus_reitingas
        self.reitingas = reitingas

    def __repr__(self):
        return f"Filmas({self.pavadinimas}, {self.trukme}, {self.zanras}, {self.rezisierius}, {self.isleidimo_metai}, {self.amziaus_reitingas})"

class AnimacinisFilmas(Filmai):
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas, animacijos_stilius, reitingas = 0):
        super().__init__(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas, reitingas)
        self.animacijos_stilius = animacijos_stilius

class DokumentinisFilmas(Filmai):
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas, tema, reitingas = 0):
        super().__init__(pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_cenzas, reitingas)
        self.tema = tema

        