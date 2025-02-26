class Sveciai:
    def __init__(self, vardas, pavarde, role):
        self.vardas = vardas
        self.pavarde = pavarde
        self.role = role

class Organizatoriai(Sveciai):
    def __init__(self, vardas, pavarde, role,  slaptazodis):
        super().__init__(vardas, pavarde, role)
        self.slaptazodis = slaptazodis

