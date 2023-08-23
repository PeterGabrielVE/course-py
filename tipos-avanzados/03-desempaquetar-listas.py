numeros = [1,2,3,4,5,6,7,8,9]

primero, segundo, *otros = numeros
print(primero, segundo, otros)

primero, *otros, ultimo = numeros
print(primero, ultimo, otros)