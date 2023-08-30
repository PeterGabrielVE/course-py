
from pprint import pprint
# 1. quitar espacio

string = "Hola mundo este es mi string"

def quita_espacios(texto):
    return [char for char in texto if char != " "]

def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] +=1
        else:
            chars_dict[char] = 1
    return chars_dict

def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )

def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repetido"
    return mensaje
    
sin_espacios = quita_espacios(string)

print(sin_espacios)

# contar en un diccionario cuanto se repiten los caracteres de un string
contados = cuenta_caracteres(sin_espacios)
pprint(contados, width=1)

#3. ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene
# tuplas 

ordenados = ordena(contados)
print(ordenados)

# 4 de un listado de tuolas, devolver la tupla con  el mayor valor
mayores = mayores_tuplas(ordenados)
print(mayores)

#5 crear un mensaje que diga:
#los caracteres que mas se repiten con 4 repeticiones son: c - d
mensaje = crea_mensaje(mayores)
print(mensaje)
