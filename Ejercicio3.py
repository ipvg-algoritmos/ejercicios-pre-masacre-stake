lista_numeros = []
while True:
    n1 = float(input("Ingrese sus números (Numero negativo para terminar): "))
    if n1 < 0:
        break
    lista_numeros.append(n1)
if lista_numeros:
    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    print(f"Su número mayor es: {mayor}")
    print(f"Su número menor es: {menor}")
else:
    print("Vuelve a intentar con otros números válidos.")
