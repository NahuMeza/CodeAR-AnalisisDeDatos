import math
import random

numero = random.randint(1, 20)
respuesta = int(input(f"¿Cuál es el raiz de {numero}? "))

if respuesta == int(math.sqrt(numero)):
    print("✅ ¡Correcto!")
else:
    print(f"❌ Incorrecto. Era {int(math.sqrt(numero))}")

# Hacer el mismo juego pero que sea adivinar la raiz de un numero

# Incorporar la logica para darle la opcion al usuario que pueda repetir el juego