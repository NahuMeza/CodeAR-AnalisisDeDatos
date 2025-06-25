import pandas as pd

# Series
# Una Serie es como una columna de datos con índice.

# serie = pd.Series([10, 20, 30, 40])
# print(serie)

# Data frame
# Un DataFrame es como una hoja de cálculo (tabla con filas y columnas).

datos = {
    'Nombre': ['Ana', 'Luis', 'Sofía', 'Camila', 'Mateo', 'Bautista'],
    'Edad': [23, 34, 29, 23, 17, 12],
}

df = pd.DataFrame(datos)

# print(df)

# Leer Archivos con pandas

# df = pd.read_csv('./Clase 3/basic.csv')  # Leer un CSV
# print(df)

# df = pd.read_excel("archivo.xlsx")  # Leer un Excel

# Ver ciertos registros

# df2 = df.head()  # Primeras n filas, 5 si no se especifica
# print(df2)

# df.tail()  # Últimas n filas, 5 si no especifica

# print(df.columns) # nombres de columnas

# print(df.shape)  # (número de filas, número de columnas)

# print(df.describe()) # resumen estadistico

# seleccionar columnas

# print(df['Edad'])  # Una sola columna
# print(df[['Nombre', 'Edad']])  # Varias columnas

# Filtrar filas

# personas_mayoresDeEdad = df[df['Edad'] > 18]  # Filtrar por condición
# print(personas_mayoresDeEdad)

# Ordenar los datos

# print(df.sort_values(by='Edad', ascending=True))

# Crear o Modificar columnas

df['Ciudad'] = ['Valencia', 'Valencia','Valencia','Valencia','Valencia','Valencia']
print(df)

# Guardar Resultados

df.to_csv("salida.csv", index=False)
