numero = 12

# 1- guardar en una variable, Verdadero si el numero es mayor que 0, y Falso si no.
# CONDICIONALES
if numero > 0:
    if(numero % 2 == 0):
        print("Es par y positivo")
else:
    print(False)

# 2- Luego, crear un ciclo for de numeros entre 10 y 20, e imprimirlos
# CICLOS
for nombre in range(10 , 21):
    print(nombre)
    if nombre % 2 == 0:
        print("ES PAR")
# ==, !=, >, <, >=, <=
# Punto estrella - dentro del ciclo, chequear si el numero es par, e imprimir "ES PAR"