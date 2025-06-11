listadenumeros = [0, 69, 22, 33, 44, 1, 92, 95, 13, 21, 22]
numero_buscado = int(input("Ingresa el número que quieres buscar: "))
if numero_buscado in listadenumeros:
    posicion = listadenumeros.index(numero_buscado)
    print(f"El número {numero_buscado} se encuentra en la lista en la posición {posicion}.")
else:
    print(f"El número {numero_buscado} no se encuentra en la lista.")
