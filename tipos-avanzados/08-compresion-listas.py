usuarios = [
     [ "Pepe", 3 ],
     [ "Maria", 7 ],
     [ "Peter", 1 ]
]

nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

nombres = [usuario[0] for usuario in usuarios]
print(nombres)

nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)