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
=> Para el caso de Jornal: 
   - el usuario debe ingresar el número de horas trabajadas y el costo por hora
   * El total del salario se calcula de multiplicar el numero de horas por costo de hora
   
   Para el caso de Prestación de Servicios

Se debe solicitar:

-El valor del contrato

-El numero de meses del contrato

-La antiguedad del empleado (años)

El salario neto, en este caso se calcula:

1 dividir el valor del contrato por el numero de meses

2 restar el 15% de valor del contraro, por concepto de EPS (Salud)

3- restar el 10% de valor del contraro, por concepto de Pension

4- si el empleado tiene una antiguedad
    igual o superiro de 10 años:
    tengra una bonificacion del 0.5%
    sobre el salario mensual 
    
=> para el contrato a termino indefinido 
se debe solicitar:
- antiguedad (años)
- grado o escalofon(1 - 5)
- el salario minimo 
el salario mensual se calcula de acuerdo 
a la siguiente tabla:
- grado 1: 1.5 SM
- grado 2: 1.7 SM
- grado 3: 2.0 SM
- grado 4: 2.5 SM
- grado 5: 3.0 SM
la bonificacion estara acorde a
los sigueintes rangos segun la antiguedad:
- entre 1 y 5 años: 1% del salario mensual
- entre 6 y 10 años: 2% del salario mensual
- superior a 10 años: 3% del salario mensual
para este caso, los descuentos de ley son:
- 25% por concepto de EPS
- 22% por concepto de pension
- 0.1% por concepto de ARL
'''
contrato = input("Ingrese el tipo de contrato:")
# inicializar variables
salario_neto = 0

if  contrato == "a":
    print("Eligió: Contrato a termino indefinido ")
    antiguedad = int(input("Ingrese antiguedad del empleado(años):"))
    grado = int(input("Ingrese grado o escalafon(1-5):"))
    salario_minimo = int(input("Ingrese valor del salario minimo:"))
    salario_mensual = 0
    if grado == 1:
        salario_mensual = salario_minimo * 1.5
    elif grado == 2:
        salario_mensual = salario_minimo * 1.7
    elif grado == 3:
        salario_mensual = salario_minimo * 2.0
    elif grado == 4:
        salario_mensual = salario_minimo * 2.5 
    elif grado == 5:
        salario_mensual = salario_minimo * 3.0
    ##calcular bonificacion
    bonificacion = 0
    if antiguedad >= 1 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.01
    if antiguedad > 5 and antiguedad <= 10:
        bonificacion = salario_mensual * 0.02
    if  antiguedad > 10:
        bonificacion = salario_mensual * 0.03
    ##descuentos de ley
    eps = salario_mensual * 0.25
    pension = salario_mensual * 0.22   
    arl = salario_mensual * 0.001 
    salario_neto = salario_mensual - eps - pension - arl + bonificacion 
    
    
    
elif contrato == "b":
    print ("Eligio: Contrato por prestacion de servicios")
    valor_contrato = int (input("ingrese el valor del contrato"))
    numero_meses = int (input("ingrese el numero de meses"))
    antiguedad = int (input("ingrese la antiguedad del empleado (años)"))
    salario_mensual = valor_contrato / numero_meses
    eps = salario_mensual * 0.15 
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.05
    salario_neto = salario_mensual - eps - pension 
    if antiguedad >=10:
        salario_neto = salario_neto + bonificacion
elif contrato == "c":
    print ("Eligio: Contrato de aprendizaje")
elif contrato == "d":
    print ("Eligio  jornal")
    numero_horas = int (input("Ingrese numero horas")) 
    valor_hora = int(input("Valor horas"))
    salario_neto = numero_horas * valor_hora
    
else: 
    print ("Contrato no válido")
print("el salario neto es:", salario_neto)
print ("FIn del programa")