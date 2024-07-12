from iproducto import Iproducto
from ingrediente import Ingrediente

class Producto(Iproducto):
    def __init__(self, nombre: str, precio_publico: float, ingrediente1: Ingrediente, ingrediente2: Ingrediente, ingrediente3: Ingrediente):
        self._nombre = nombre
        self._precio = precio_publico
        self._ingrediente1 = ingrediente1
        self._ingrediente2 = ingrediente2
        self._ingrediente3 = ingrediente3
    
    # Implementar métodos abstractos
    def calcular_calorias(self):
        pass

    def calcular_costo(self):
        pass

    def calcular_rentabilidad(self):
        pass

    # Getters y setters
    def get_nombre(self) -> str:
        return self._nombre
    
    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_precio(self) -> float:
        return self._precio
    
    def set_precio(self, precio: float):
        self._precio = precio

    def get_ingredientes(self):
        return [self._ingrediente1, self._ingrediente2, self._ingrediente3]




