
motor_encendido = True
temperatura = 70  

if temperatura > 80:
    motor_encendido = False  
# Estado inicial del motor
motor_encendido = True
# Temperatura actual de la máquina
temperatura = 85  # Puedes cambiar este valor para probar diferentes escenarios

# Verificamos la temperatura
if temperatura > 80:
    motor_encendido = False  # Apagamos el motor
    print("La temperatura ha superado los 80 grados.")
    print("El motor se ha apagado automáticamente.")
else:
    print("La temperatura está dentro del rango seguro.")
    print("El motor sigue encendido.")



# Estado final del motor
if motor_encendido:
    print("Estado del motor: Encendido")
else:
    print("Estado del motor: Apagado")

print("Fin del programa")