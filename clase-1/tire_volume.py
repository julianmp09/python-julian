import math
from datetime import datetime

ancho_del_neumatico = float(input("Ingrese el ancho del neumatico en mm (ex 205): "))
relacion_del_aspecto = float(input("Ingrese la relación de aspecto del neumático (ex 60): "))
diametro_del_neumatico = float(input("Ingrese el diámetro de la rueda en pulgadas (ex 15):"))

def calcular_el_volumen_del_neumatico (ancho,relacion_de_aspecto, diametro):
    """Esta funcion calcula el volumen del neumatico"""
    numerador1 = math.pi * ancho ** 2 * relacion_de_aspecto 
    numerador2 = ancho * relacion_de_aspecto + 2540 * diametro
    denominador = 10000000000
    volumen = numerador1 * numerador2 / denominador
    return volumen
    
current_date_and_time = datetime.now()



print(f"El volumen aproximado es de {calcular_el_volumen_del_neumatico(ancho_del_neumatico, relacion_del_aspecto, diametro_del_neumatico):.2f} litros")

print()

print(f"Cada precio del neumatico es diferente segun su ancho, relacion del aspecto y diametro. Usted tiene {ancho_del_neumatico:.0f}, {relacion_del_aspecto:.0f}, {diametro_del_neumatico:.0f}")
print()
# I created the if statement for said the price the user according to your needs.
if ancho_del_neumatico >= 350 and (relacion_del_aspecto >= 80 or diametro_del_neumatico >= 30):
    precio = 500
    print(f"Usted pagara: ${precio} dolares.")
elif ancho_del_neumatico >= 250 and (relacion_del_aspecto >= 70 or diametro_del_neumatico >= 25):
    precio = 300
    print(f"Usted pagara: ${precio} dolares.")
elif ancho_del_neumatico >= 200 and (relacion_del_aspecto >= 65 or diametro_del_neumatico >= 20):
    precio = 200
    print(f"Usted pagara: ${precio} dolares.")
elif ancho_del_neumatico >= 150 and (relacion_del_aspecto >= 50 or diametro_del_neumatico >= 15):
    precio = 100
    print(f"Usted pagara: ${precio} dolares.")
else:
    print("No hasy presupuesto")    
print()


pregunta = input("usted quiere comprar? (si/no) ")


if pregunta != "si":
    print("Gracias vuelva pronto")
    telefono_celular = None
else:
    telefono_celular = int(input("Por favor añada su numero. ex +54-11-658458: "))
    print("su orden a sido registrada")
    


with open ("volumenes.txt", "at") as volumen_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {ancho_del_neumatico:.0f}, {relacion_del_aspecto:.0f}, {diametro_del_neumatico:.0f}, {calcular_el_volumen_del_neumatico(ancho_del_neumatico, relacion_del_aspecto, diametro_del_neumatico):.2f},         {telefono_celular}", file=volumen_file)




