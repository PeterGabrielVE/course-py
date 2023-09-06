class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def __del__(self):
        print(f"Chao perro :( ")
        
    def habla(self):
       print(f"{self.nombre} dice: Gaua!!")


perro1 = Perro("titi", 5)

print(perro1)

perro2 = Perro("titina", 8)
del perro2