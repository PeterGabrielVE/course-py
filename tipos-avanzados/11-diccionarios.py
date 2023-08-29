punto = {"x":25, "y":50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

usuarios = [
    {"Nombre": "Sara", "Edad": 27,"Documento": 1003882 },
    {"Nombre": "Peter", "Edad": 27,"Documento": 1003882 },
]
for usuario in usuarios:
    print(usuario["Nombre"])