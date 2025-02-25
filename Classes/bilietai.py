#  bilietai.py

# class Bilietai:
#     def __init__(self, eile, vieta):
#         self.eile = eile
#         self.vieta = vieta

# class Vip_bilietai(Bilietai):
#     def __init__(self, eile, vieta, reitingas):
#         super.__init__(self, eile, vieta)
#         self.reitingas = reitingas
        
class BilietuRezervacija:
    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas
        self.vietos = 120
        self.rezervuotos_vietos = 0
        self.pajamos = 0.0

    def rezervuoti_vieta(self, vietu_skaicius):
        if vietu_skaicius <= 0:
            raise ValueError("Vietų skaičius turi būti teigiamas.")
        if self.rezervuotos_vietos + vietu_skaicius > self.vietos:
            raise ValueError("Nepakanka laisvų vietų.")
        self.rezervuotos_vietos += vietu_skaicius

    def pirkti_bilieta(self, vietu_skaicius, kaina_vienam_bilietui):
        self.rezervuoti_vieta(vietu_skaicius)
        self.pajamos += vietu_skaicius * kaina_vienam_bilietui

    def atšaukti_rezervacija(self, vietu_skaicius):
        if vietu_skaicius <= 0 or vietu_skaicius > self.rezervuotos_vietos:
            raise ValueError("Netinkamas vietų skaičius atšaukimui.")
        self.rezervuotos_vietos -= vietu_skaicius
        


