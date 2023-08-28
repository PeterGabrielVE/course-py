numeros = [ 2, 4, 1, 45, 32, 75, 24, 51 ]

#numeros.sort(reverse=True)
numeros2 = sorted(numeros)
print(numeros)
print(numeros2)

usuarios = [ 
            [ 4, "Pepe" ],
            [ 1, "Maria" ],
            [ 5, "Peter" ]
]

usuarios.sort()
print(usuarios)

usuarios2 = [ 
            [ "Pepe", 3 ],
            [ "Maria", 7 ],
            [ "Peter", 1 ]
]

def ordena(elemento):
    return elemento[1]

usuarios2.sort( key=ordena, reverse=True )
print(usuarios2)