# Solicitar al usuario el estrato, la edad y el valor de la matrícula
estrato = int(input("Ingrese su estrato (1 o 2): "))
edad = int(input("Ingrese su edad: "))
valor_matricula = float(input("Ingrese el valor de la matrícula: "))

# Inicializar el descuento
descuento = 0

# Calcular el descuento según las condiciones
if estrato == 1:
    if edad < 18:
        descuento = 0.20 * valor_matricula  # 20% de descuento
    else:
        descuento = 0.15 * valor_matricula  # 15% de descuento
elif estrato == 2:
    if edad < 18:
        descuento = 0.10 * valor_matricula  # 10% de descuento
    else:
        descuento = 0.05 * valor_matricula  # 5% de descuento
else:
    print("Estrato no válido. Solo se aceptan estratos 1 y 2.")

# Calcular el precio a pagar
precio_a_pagar = valor_matricula - descuento

# Mostrar el resultado
print(f"El valor del descuento es: {descuento:.2f}")
print(f"El precio a pagar por la matrícula es: {precio_a_pagar:.2f}")