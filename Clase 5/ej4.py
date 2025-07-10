import matplotlib.pyplot as plt

# Copiar el diccionario del anterior ejercicio y usarlo para hacer un grafico

dicti = {
    "Independiente":[1 , 2 , 3],
    "Dependiente": [10 , 20 , 10]
}

plt.plot(dicti["Independiente"], dicti["Dependiente"] ,marker="*", color="orange")
plt.title("Grafico de Independiente vs Dependiente")
plt.xlabel("Independiente")
plt.ylabel("Dependiente")
plt.show()

# recordemos que los graficos son de la forma: 
# plt.plot(Variable independiente, variable dependiente, color='color')

# Agregarle titulo y nombre a las variables (plt.title, plt.xlabel, plt.ylabel)

