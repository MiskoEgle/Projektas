import Functions.filmu_registracija as fil_reg
import Functions.filmu_paieska as paieska
import Functions.filmu_reitingavimas as reiting
import Functions.seansu_meniu as seans
import Functions.rezervacijos_meniu as reservacija

def svecio_meniu():
    while True:
        print("Pasirinkite norimą funkciją")
        print("1. Filmų peržiūra ir paieška")
        print("2. Bilietų rezervacija")
        print("3. Filmų reitingavimas")
        print("4. Išeiti")
        
        pasirinkimas = input("Pasirinkite veiksmą: ")
            
        if pasirinkimas == '1':
            paieska.filmu_perziura_ir_paieska()
        elif pasirinkimas == '2':
            reservacija.rezervaciju_meniu()
        elif pasirinkimas == '3':
            reiting.filmu_reitingavimas()
        elif pasirinkimas == '4':
            print("\nSvečias atsijungė\n")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
    
def organizatoriu_meniu():
    while True:
        print("Pasirinkite norimą funkciją")
        print("1. Filmų registracija")
        print("2. Filmų peržiūra ir paieška")
        print("3. Seansų planavimas")
        print("4. Išeiti")
        
        pasirinkimas = input("Pasirinkite veiksmą: ")
            
        if pasirinkimas == '1':
            fil_reg.filmu_registravimo_meniu()
        elif pasirinkimas == '2':
            paieska.filmu_perziura_ir_paieska()
        elif pasirinkimas == '3':
            seans.seanso_meniu()
        elif pasirinkimas == '4':
            print("\nOrganizatorius atsijungė\n")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
            

