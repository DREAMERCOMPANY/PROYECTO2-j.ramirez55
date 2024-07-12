from producto import Producto
from funciones import *
from ingrediente import Ingrediente

class Malteada(Producto):
    def __init__(self, nombre: str, precio_publico: float, ingrediente1: Ingrediente, ingrediente2: Ingrediente, ingrediente3: Ingrediente, volumen: float):
        super().__init__(nombre, precio_publico, ingrediente1, ingrediente2, ingrediente3)
        self.__volumen = volumen
        self._calorias = [ingrediente1.get_calorias(), ingrediente2.get_calorias(), ingrediente3.get_calorias()]

    # Getters y setters
    def get_volumen(self) -> float:
        return self.__volumen
    
    def set_volumen(self, volumen: float):
        self.__volumen = volumen
    
    # Implementación de los métodos abstractos de Producto
    def calcular_calorias(self):
        sumaCalorias = 0
        for caloria in self._calorias:
            sumaCalorias += caloria
        return sumaCalorias + 200
    
    def calcular_costo(self):
        costoIngrediente1 = {"nombre": self._ingrediente1.get_nombre(), "precio": self._ingrediente1.get_precio()}
        costoIngrediente2 = {"nombre": self._ingrediente2.get_nombre(), "precio": self._ingrediente2.get_precio()}
        costoIngrediente3 = {"nombre": self._ingrediente3.get_nombre(), "precio": self._ingrediente3.get_precio()}
        return calcular_costo(costoIngrediente1, costoIngrediente2, costoIngrediente3)
    
    def calcular_rentabilidad(self):
        costoIngrediente1 = {"nombre": self._ingrediente1.get_nombre(), "precio": self._ingrediente1.get_precio()}
        costoIngrediente2 = {"nombre": self._ingrediente2.get_nombre(), "precio": self._ingrediente2.get_precio()}
        costoIngrediente3 = {"nombre": self._ingrediente3.get_nombre(), "precio": self._ingrediente3.get_precio()}
        return calcular_rentabilidad(self._precio, costoIngrediente1, costoIngrediente2, costoIngrediente3)
