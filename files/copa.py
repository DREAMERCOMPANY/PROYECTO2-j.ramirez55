from producto import Producto
from funciones import *
from ingrediente import Ingrediente

class Copa(Producto):
    def __init__(self, nombre: str, precio_publico: float, ingrediente1: Ingrediente, ingrediente2: Ingrediente, ingrediente3: Ingrediente, tipo_vaso: str):
        super().__init__(nombre, precio_publico, ingrediente1, ingrediente2, ingrediente3)
        self.__tipoVaso = tipo_vaso
        self._calorias = [ingrediente1.get_calorias(), ingrediente2.get_calorias(), ingrediente3.get_calorias()]

    # Getters y setters
    def get_tipoVaso(self) -> str:
        return self.__tipoVaso
    
    def set_tipoVaso(self, vaso: str):
        self.__tipoVaso = vaso
    
    # Implementación de los métodos abstractos de Producto
    def calcular_calorias(self):
        return contar_calorias(self._calorias)
    
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



   
