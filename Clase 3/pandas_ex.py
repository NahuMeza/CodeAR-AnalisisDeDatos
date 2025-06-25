import pandas as pd

# Series
# Una Serie es como una columna de datos con índice.

serie = pd.Series([10, 20, 30, 40])
print(serie)

# Data frame
# Un DataFrame es como una hoja de cálculo (tabla con filas y columnas).

# datos = {
#     'Nombre': ['Ana', 'Luis', 'Sofía'],
#     'Edad': [23, 34, 29]
# }

# df = pd.DataFrame(datos)
# print(df)

# Leer Archivos con pandas

# df = pd.read_csv("archivo.csv")  # Leer un CSV
# df = pd.read_excel("archivo.xlsx")  # Leer un Excel

# Ver ciertos registros

# df.head()  # Primeras 5 filas
# df.tail(3)  # Últimas 3 filas

# print(df.columns) # nombres de columnas

# df.shape  # (número de filas, número de columnas)

# print(df.describe()) # resumen estadistico

# seleccionar columnas

# df['Edad']  # Una sola columna
# df[['Nombre', 'Edad']]  # Varias columnas

# Filtrar filas

# df[df['Edad'] > 25]  # Filtrar por condición

# Ordenar los datos

# df.sort_values(by='Edad', ascending=False)

# Crear o Modificar columnas

# df['Nueva_Columna'] = df['Edad'] * 2 

# Guardar Resultados

# df.to_csv("salida.csv", index=False)
