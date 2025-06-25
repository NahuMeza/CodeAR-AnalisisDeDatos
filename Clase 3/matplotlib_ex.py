# lineas
import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [3, 7, 2, 5, 9]

# plt.plot(x, y, color='blue', marker='o', linestyle='--', label='referencia')
# plt.title('Gráfico de Líneas')
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# # plt.legend()
# plt.grid()
# plt.show()

# Barras horizontales y verticales

# categorias = ['A', 'B', 'C', 'D']
# valores = [23, 17, 35, 29]

# plt.bar(categorias, valores, color='orange')
# plt.title('Gráfico de Barras')
# plt.show()

# -----

# plt.barh(categorias, valores, color='green')
# plt.title('Barras Horizontales')
# plt.show()

# Grafico de dispersion
# ver la relacion entre dos variables

# x = [5, 7, 8, 7, 2, 17, 2, 9]
# y = [99, 86, 87, 88, 100, 86, 103, 87]

# plt.scatter(x, y, color='red')
# plt.title('Gráfico de Dispersión')
# plt.show()

# Graficos de pastel

# tamaños = [35, 25, 25, 15]
# etiquetas = ['Manzanas', 'Bananas', 'Cerezas', 'Dátiles']

# plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=140)
# plt.title('Gráfico de Pastel')
# plt.show()

# varios graficos
# plt.subplot(1, 2, 1)  # 1 fila, 2 columnas, primer gráfico
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.title('Gráfico 1')

# plt.subplot(1, 2, 2)  # Segundo gráfico
# plt.bar(['A', 'B', 'C'], [3, 7, 5])
# plt.title('Gráfico 2')

# plt.show()