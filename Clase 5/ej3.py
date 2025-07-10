# 1- Crear un diccionario que tenga dos elementos, Independiente, dependiente.
dicti = {
    "Independiente":[1 , 2 , 3],
    "Dependiente": [10 , 20 , 30]
}
print(dicti)

# el valor de ambos elementos debe ser una lista de numeros. Independiente del 1 al 3
# y dependiente los valores que mas guste

# 2- imprimir los valores independientes, y luego los valores dependiente.
print("Valores de Independiente", dicti["Independiente"])

print("Valores de Dependiente", dicti["Dependiente"])
# 3- Imprimir el segundo elemento de dependiente.
print(dicti["Dependiente"][1])

dicti["Independiente"].append(4)
dicti["Dependiente"].append(40)
print(dicti)