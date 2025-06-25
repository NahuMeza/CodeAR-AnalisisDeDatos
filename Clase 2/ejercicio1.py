
dict = {
    'Nombre': ['Ana', 'Luis', 'Sofía', 'Camila'], 
    'Edad': [23, 34, 29, 23]
}

def imprimir_personas(dict):
    # for dato in dict:
    #     if dato == "Nombre":
    #         for nombre in dict[dato]:
    #             print(nombre)

    for nombre in dict["Nombre"]:
        print(nombre)
        
    return None

def imprimir_edades(dict):
    #imprimir las edades de las personas
    for edad in dict["Edad"]:
        print(edad)
    return None

def imprimir_promedio(dict):
    #imprimir el promedio de las edades de las personas
    suma = 0
    for edad in dict["Edad"]:
       suma = suma + edad
    promedio = suma / len(dict["Edad"])
    print(promedio)

# ciclo 1: edad -> dict -> [0]. edad = 23; -> {suma = 0 + 23 = 23}
# ciclo 2: edad -> dict -> [1]. edad = 34; -> {suma = 23 + 34 = 57}
# ciclo 3: edad -> dict -> [2]. edad = 29; -> {suma = 57 + 29 = 86}
# ciclo 4: edad -> dict -> [3] !!!!.
# fin del ciclo

imprimir_personas(dict)
imprimir_edades(dict)
imprimir_promedio(dict)
