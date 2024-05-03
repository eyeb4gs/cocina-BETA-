import os

def limpiar():
    os.system("cls")
    
def platos():
    print("""
1) Huevo Frito
""")
    
#======= I N I C I O =================

limpiar()
print("🙋 <(Hola, te ayudare en la cocina, ¿Cuál es tu nombre?)")
usuario = input()
limpiar()

print("Hola ",usuario,",¿Qué prepararas hoy?\n")
platos()

input("""
Digita la opción:       
""")


    
    