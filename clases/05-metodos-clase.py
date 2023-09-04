class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @classmethod
    def habla(cls):
        print("Guau")

    @classmethod
    def factory(cls):
        return cls("pepe feliz", 4)

Perro.habla()

Perro3 = Perro.factory()

print(Perro3.nombre)
