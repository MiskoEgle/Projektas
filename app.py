# app.py

# import Classes.vartotojai as vart
# import Functions.vartotojo_registracija as reg
# import Functions.filmu_registracija as fil_reg
# import Functions.filmu_paieska as paieska



# if __name__ == "__main__":
#     try:
#         reg.vartotojo_meniu()
#         fil_reg.filmu_restravimo_meniu()
#         paieska.filmu_perziura_ir_paieska()
#     except Exception as e:
#         print(f"Klaida: {e}")
    

import Functions.vartotojo_registracija as regist

if __name__== "_main_":
    regist.vartotojo_meniu()

