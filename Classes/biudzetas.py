#  biudzetas.py

# class Irasas:
#     def __init__(self, suma):
#         self.suma = suma

# class PajamuIrasas(Irasas):
#     def __init__(self, suma, žiurovas, įsigytas_bilietas):
#         super().__init__(suma)
#         self.siuntejas = žiurovas
#         self.isigytas_bilietas = įsigytas_bilietas
        

# class IslaiduIrasas(PajamuIrasas):
#     def __init__(self, suma, žiurovas, įsigytas_bilietas, rezervacijos_atsaukimas):
#         super().__init__(suma, žiurovas, įsigytas_bilietas)
#         self.papildoma_informacija = rezervacijos_atsaukimas

# class Biudzetas:
#     def __init__(self):
#         self.zurnalas = []

#     def prideti_pajamas(self, suma, siuntejas, papildoma_informacija):
#         irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
#         self.zurnalas.append(irasas)

#     def prideti_islaidas(self, suma, atsiskaitymo_budas, isigytas_bilietas):
#         irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigytas_bilietas)
#         self.zurnalas.append(irasas)

#     def balansas(self):
#         balansas = 0
#         for irasas in self.zurnalas:
#             if isinstance(irasas, PajamuIrasas):
#                 balansas += irasas.suma
#             elif isinstance(irasas, IslaiduIrasas):
#                 balansas -= irasas.suma
#         return balansas

#     def gauti_ataskaita(self):
#         ataskaita = []
#         for irasas in self.zurnalas:
#             if isinstance(irasas, PajamuIrasas):
#                 ataskaita.append(f"Pajamos: {irasas.suma}, Žiurovas: {irasas.siuntejas}, Info: {irasas.isigytas_bilietas}")
#             elif isinstance(irasas, IslaiduIrasas):
#                 ataskaita.append(f"Išlaidos: {irasas.suma},Žiurovas: {irasas.siuntejas}, Info: {irasas.isigytas_bilietas}")
#         return ataskaita
    
# def parodyti_pajamas(seansai):
#     bendros_pajamos = sum(seansas.pajamos for seansas in seansai.values())
#     print(f"Bendros pajamos: {bendros_pajamos:.2f} EUR")

# # Example of showing total revenue
# # parodyti_pajamas(seansas)


class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, žiurovas, įsigytas_bilietas):
        super().__init__(suma)
        self.siuntejas = žiurovas
        self.isigytas_bilietas = įsigytas_bilietas
        

class IslaiduIrasas(PajamuIrasas):
    def __init__(self, suma, žiurovas, įsigytas_bilietas, rezervacijos_atsaukimas):
        super().__init__(suma, žiurovas, įsigytas_bilietas)
        self.papildoma_informacija = rezervacijos_atsaukimas

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamas(self, suma, siuntejas, papildoma_informacija):
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)

    def prideti_islaidas(self, suma, atsiskaitymo_budas, isigytas_bilietas):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigytas_bilietas)
        self.zurnalas.append(irasas)

    def balansas(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            elif isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return balansas

    def gauti_ataskaita(self):
        ataskaita = []
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                ataskaita.append(f"Pajamos: {irasas.suma}, Žiurovas: {irasas.siuntejas}, Info: {irasas.isigytas_bilietas}")
            elif isinstance(irasas, IslaiduIrasas):
                ataskaita.append(f"Išlaidos: {irasas.suma},Žiurovas: {irasas.siuntejas}, Info: {irasas.isigytas_bilietas}")
        return ataskaita
    
def parodyti_pajamas(seansai):
    bendros_pajamos = sum(seansas.pajamos for seansas in seansai.values())
    print(f"Bendros pajamos: {bendros_pajamos:.2f} EUR")

# Example of showing total revenue
# parodyti_pajamas(seansas)