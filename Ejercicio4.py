contador = 0
suma = 0
while True:
    n1 = float(input("Insertar 3 número (El tercero debe ser negativo): "))
    if n1 < 0:
        break
    suma += n1
    contador += 1
if contador > 0:
    restulado_promedio = suma / contador
    resultaod_promedio = round(restulado_promedio, 2)
    print("El promedio es:", restulado_promedio)
else:
    print("Vuelve a intentar con otros números.")