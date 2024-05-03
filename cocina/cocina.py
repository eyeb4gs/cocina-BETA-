import os
import time

def limpiar():
    os.system("cls")
    
tiempodeespera = 1
    
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

opcion = input("""
Digita la opción:       
""")

if opcion == "1":
    limpiar()
    print(""""
 ________________________
|           _____        |
|          |     |       |
|          |  🍌 |       |
|          |_____|_______|
|          |           | |
|          |  🍇 🥚 🍏 | |
|          |  🍇 🍎 🍊 | |
|__________|___________|_|
|          |   _____   | |
|          |  |_____|  | |
|__________|___________|_|
""")
    time.sleep(tiempodeespera)
    input("PRESIONA ENTER PARA AGARRAR EL HUEVO")
    limpiar()
    print(""""
 ________________________
|           _____        |
|          |     |       |
|          |  🍌 |       |
|          |_____|_______|
|          |           | |
|          |  🍇    🍏 | |
|          |  🍇 🍎 🍊 | |
|__________|___________|_|
|          |   _____   | |
|          |  |_____|  | |
|__________|___________|_|
""")
    time.sleep(tiempodeespera)
    limpiar()

    
    
    
    
    
