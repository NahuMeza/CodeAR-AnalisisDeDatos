# lineas
import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [3, 7, 2, 5, 9]

# x_prima = [3,6,7,8]
# y_prima= [12,5,7,2]

# plt.plot(x, y, color='red', marker='o', label='referencia')
# plt.plot(x_prima, y_prima,color = 'green', label='prima')
# plt.title('Gráfico de Líneas')
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.legend()
# plt.grid()
# plt.show()

# Barras horizontales y verticales

# categorias = ['A', 'B', 'C', 'D']
# valores = [23, 17, 35, 29]

# plt.bar(categorias, valores, color=['red','orange','blue','pink'])
# plt.title('Gráfico de Barras')
# plt.xlabel('Categorias')
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




# EJEMPLO REAL
# # Datos
# carga_utilpt2c2 =     [0,0.42,0.46,0.77,2.57,17.22,29.84,37.85,45.42,50.87,67.8,75.75]
# carga_ofrecidapt2c2 = [0,1,2,4,5,6,7,8,9,10,15,20]
# #0.4
# carga_utilpt2c1 =     [0,0.39,0.42,0.71,2.31,17.1,29.61,37.80,45.32,50.25,67.22,75.15]
# carga_ofrecidapt2c1 = [0,1,2,4,5,6,7,8,9,10,15,20]
# # Graficar
# plt.plot(carga_ofrecidapt2c2, carga_utilpt2c2, marker='o', linestyle='-', color='b', label='Carga útil c2')

# plt.plot(carga_ofrecidapt2c1, carga_utilpt2c1, marker='o', linestyle='-.', color='orange', label='Carga útil c1')
# # Etiquetas
# plt.xlabel('Carga ofrecida')
# plt.ylabel('Average Delay')
# plt.title('Average Delay vs. Carga ofrecida')
# plt.legend()
# plt.grid(True)
# plt.margins(x=0.1, y=0.1)

# # Mostrar
# plt.show()