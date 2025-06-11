listadenumeros= []
while True:
    numero = float(input("Por favor ingrese los números (El último número debe ser negativo): "))
    if numero < 0:
        break
    listadenumeros.append(numero)
if listadenumeros:
    mayor = max(listadenumeros)
    menor = min(listadenumeros)
    print(f"Su número mayor es: {mayor}")
    print(f"Su número menor es: {menor}")
else:
    print("Vuelve a intentar con otros números válidos.")
