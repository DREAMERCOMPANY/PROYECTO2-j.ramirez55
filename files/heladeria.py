from producto import Producto
from ingrediente import Ingrediente
from base import Base

class Heladeria:
    def __init__(self, producto1: Producto, producto2: Producto, producto3: Producto, producto4: Producto):
        self._producto1 = producto1
        self._producto2 = producto2
        self._producto3 = producto3
        self._producto4 = producto4
        self._productos = [producto1, producto2, producto3, producto4]
        self.__ingredientes = []
        self._ventas_del_dia = 0.0
    
    def get_ingredientes(self):
        return self.__ingredientes
    
    def add_ingrediente(self, ingrediente: Ingrediente):
        if ingrediente in self.__ingredientes:
            print(f"El ingrediente {ingrediente.get_nombre()} ya ha sido añadido.")
        else:
            self.__ingredientes.append(ingrediente)
            print(f"Ingrediente {ingrediente.get_nombre()} añadido correctamente.")
    
    def vender(self, nombreProducto: str) -> bool:
        # Buscar el producto por nombre
        producto_a_vender = None
        for producto in self._productos:
            if producto.get_nombre() == nombreProducto:
                producto_a_vender = producto
                break
        
        # Si el producto no existe, retornar False
        if producto_a_vender is None:
            print(f"El producto {nombreProducto} no está disponible.")
            return False
        
        # Verificar que haya suficientes ingredientes para hacer el producto
        ingredientes_necesarios = producto_a_vender.get_ingredientes()
        complementos_disponibles = True

        for ingrediente in ingredientes_necesarios:
            if ingrediente.get_inventario() < 1:
                complementos_disponibles = False
                break
        
        base_disponible = False
        for ingrediente in self.__ingredientes:
            if isinstance(ingrediente, Base):
                if ingrediente.get_inventario() >= 0.2:
                    base_disponible = True

        if not (complementos_disponibles and base_disponible):
            print(f"No hay suficientes ingredientes para hacer el producto {nombreProducto}.")
            return False
        
        # Restar las cantidades necesarias de los ingredientes
        for ingrediente in ingredientes_necesarios:
            ingrediente.set_inventario(ingrediente.get_inventario() - 1)
        
        for ingrediente in self.__ingredientes:
            if isinstance(ingrediente, Base):
                ingrediente.set_inventario(ingrediente.get_inventario() - 0.2)
        
        # Sumar el precio del producto a las ventas del día
        self._ventas_del_dia += producto_a_vender.get_precio()
        print(f"Producto {nombreProducto} vendido por {producto_a_vender.get_precio()}. Ventas del día: {self._ventas_del_dia}.")
        
        return True


