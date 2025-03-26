'''
Actividad 3:
elabore un programa que 
permita calcular el salario
neto de un empleado,
despues de descontar los 
descuentos por conceptos de:
Salud, Pension, ARL
1. El programa debe solicitar
el tipo de empleado:
a - Contrato a termino indefenido
b - Contrato por prestacion 
    de servicios
c - Contrato de aprendizaje
d - Contrato por Jornal(freelance)
'''
contrato = input("Ingrese el tipo de contrato:")
if contrato == "a":
    print ("Eligio: Contrato a termino indefinido")
elif contrato == "b":
    print ("Eligio: Contrato por prestacion de servicios")
elif contrato == "c":
    print ("Eligio: Contrato de aprendizaje")
elif contrato == "d":
    print ("Eligio: Contrato por jornal(freelance)")