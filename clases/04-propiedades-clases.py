class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def habla(self):
        print(f"{self.edad} dice : Guau")

mi_perro = Perro("Pepe", 1)
mi_perro2 = Perro("Pepita", 2)

print(mi_perro.nombre)
print(mi_perro2.nombre)

print(mi_perro.habla())
print(mi_perro2.habla())

print(mi_perro2.patas)