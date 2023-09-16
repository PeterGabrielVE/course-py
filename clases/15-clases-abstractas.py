from abc import ABC, abstractmethod

class Model(ABC):
    tabla = False
    
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")
    
    @property
    @abstractmethod
    def tabla(self):
        pass
    
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

class Usuario(Model):
    tabla = "usuario"


usuario = Usuario()

usuario.guardar()