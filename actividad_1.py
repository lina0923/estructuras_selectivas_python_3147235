motor_encendido = True
temperatura = 70  

if temperatura > 80:
    motor_encendido = False  
    print("La temperatura ha superado los 80 grados.")
    print("El motor se ha apagado automáticamente.")
else:
    print("La temperatura está dentro del rango seguro.")
    print("El motor sigue encendido.")


if motor_encendido:
    print("Estado del motor: Encendido")
else:
    print("Estado del motor: Apagado")

print("Fin del programa")