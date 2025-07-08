
variable = 12

print(variable)

variable = "hola"

print(variable)

variable = [1,2,3,4]
longitud = len(variable)

print(variable, "cantidad: ", longitud)


dict = {
    'Nombre': ['Ana', 'Luis', 'Sofía', 'Camila'], 
    'Edad': [23, 34, 29, 23]
}

print(dict["Nombre"])

for i in range(0,10):
    print(i)

for nombre in dict["Nombre"]:
    print(nombre)

