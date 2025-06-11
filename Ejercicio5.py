martiz = []
print("Ingrese los elementos de la matriz 3x3 (números enteros):")
for i in range(3):
    fila = []
    for j in range(3):
        numero = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

positivos = 0
negativos = 0
ceros = 0

suma_diagonal_principal = 0
suma_diagonal_secundaria = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] > 0:
            positivos += 1
        elif matriz[i][j] < 0:
            negativos += 1
        else:
            ceros += 1
        
        if i == j:
            suma_diagonal_principal += matriz[i][j]
        
        if i + j == 2:
            suma_diagonal_secundaria += matriz[i][j]
print(f"Cantidad de positivos: {positivos}")
print(f"Cantidad de negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")
if suma_diagonal_principal > suma_diagonal_secundaria:
    print("La suma de la diagonal principal es mayor que la de la diagonal secundaria.")
elif suma_diagonal_principal < suma_diagonal_secundaria:
    print("La suma de la diagonal principal es menor que la de la diagonal secundaria.")
else:
    print("La suma de ambas diagonales es igual.")