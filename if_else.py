'''
if else:
Sirve para determinar dos caminos 
de ejecucion, basados en la evaluacion
de una condici9onal sintaxis:
if condicional
    instruccion1
    intsruccion2
else:
    instruccion1
    instruccion2
'''


#ejemplo:
#elabore un programa en python 
#que determine si una persona
#es mayor o menor de edad
#y por tanto, habilitada para 
#votar


edad = int (input ("ingrese su edad"))
documento = input ("tiene documento (SI/NO):")
if edad >= 18 and documento=="SI":
    print ("Usted es mayor de edad")
    print ("Puede votar")

else:
    print ("Usted es menor de edad")
    print("o")
    print ("No Puede votar")
print ("fin del programa")

