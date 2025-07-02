import matplotlib.pyplot as plt
# Ejercicio 1 – Gráfico de Líneas básico
# Crea un gráfico de líneas que muestre la evolución de la temperatura durante 5 días.

# Días: 1, 2, 3, 4, 5

# Temperaturas: 22, 24, 20, 23, 25

# Agrega título y etiquetas a los ejes.

dias = [1,2,3,4,5]
temperaturas = [22,24,20,23,25]

plt.plot(dias, temperaturas)
plt.title("EVOLUCION DE TEMPERATURAS CHUI Q FRIO")
plt.xlabel("dias")
plt.ylabel("temperaturas")
plt.show()


# Ejercicio 2 – Gráfico de Barras
# Muestra un gráfico de barras con la cantidad de ventas de tres productos:

# Producto A: 50 ventas

# Producto B: 80 ventas

# Producto C: 30 ventas

# Ventas = [50, 30, 80]
# Productos = ['A', 'C', 'B']

# plt.bar(Productos, Ventas, color='blue')
# plt.show()