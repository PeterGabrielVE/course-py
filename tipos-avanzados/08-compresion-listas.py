usuarios = [
     [ "Pepe", 3 ],
     [ "Maria", 7 ],
     [ "Peter", 1 ]
]

nombres = []
#for usuario in usuarios:
#    nombres.append(usuario[0])
#print(nombres)

#nombres = [usuario[0] for usuario in usuarios]
#print(nombres)

#nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
#print(nombres)

#nombres = list(map(lambda usuario: usuario[0], usuarios))
nombres = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres)