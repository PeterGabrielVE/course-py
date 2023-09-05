class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self):
        self.__nombre = nombre

    def habla(self):
        print("Guau")

    @classmethod
    def factory(cls):
        return cls("pepe feliz", 4)


perro1 = Perro.factory()
perro1.habla()
print(perro1.__dict__)
