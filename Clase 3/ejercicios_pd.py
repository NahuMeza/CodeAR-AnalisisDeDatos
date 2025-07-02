import pandas as pd

# Ejercicio 1 – Crear un DataFrame
# Crea un DataFrame con la siguiente información de personas:

# Nombre	Edad	Ciudad
# Ana	23	Madrid
# Luis	34	Barcelona
# Sofía	29	Valencia

data = {
    'Nombre': ['Ana', 'Luis', 'Sofía'],
    'Edad': [23, 34, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(data)

# Mostrá el DataFrame completo.

#print(df)

# Ejercicio 2 – Agregar una columna
# Agregá una nueva columna llamada Salario con los valores: 2000, 2500, 2200.

df['Salario'] = [2000, 2500, 2200]

# Mostrá el DataFrame actualizado.
#print(df)

# Ejercicio 4 – Ordenar por Salario
# Ordená el DataFrame por la columna Salario de mayor a menor.

df_new = df.sort_values(by='Salario', ascending= False)
print(df_new)
print(df)

# Ejercicio 6 - Guardar en CSV
# Guarda el DataFrame resultante en un archivo csv llamado resultado.csv

df.to_csv('FIN.csv', index = False)