'''
if anidados:
if dentro de otro if
syntax
if condicion1:
    if condicion2:
        print("mensaje1")
    elif conficion3:
        print("mensaje2")
    elif conficion4:
        print("mensaje3")
    elif conficion5:
        print("mensaje4")
    else
        print ("mensaje5")
no confuncir con elif (if en cascada)
'''

#EJEMPLO 1:
#Modifique el ejercicio de la edad
#para las siguientes condiciones
#1. si es mayor de 18 años
# pero no tiene documento, no puede votar
#  de lo contrario si uede votar
#2. si es menor de 18 años
#  no puede votar
# utlice estructura de if anidados

edad= int (input("ingrese su edad:"))
if edad >=18:
        documento = input ("tiene documento? (si/no): ")
        if documento == "si":
            print ("puede votar")
        else:
            print ("no puede votar")
else:
    print ("no puede votar")