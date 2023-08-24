mascotas = ["Pelusa", "Pulga", "Felipe", "Terry", "Kike"]

mascotas.insert(1, "Melvin")
mascotas.append("Melvin Feliz")
mascotas.append("Melvin Triste")

mascotas.remove("Pulga")
mascotas.pop()

del mascotas[0]
print(mascotas)

mascotas.clear()
print(mascotas)