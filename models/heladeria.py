from models.ingredientes import Ingredientes
from models.productos import Productos

# Clase Heladeria para manejar lógica de negocio
class Heladeria:
    def __init__(self):
        self.ingredientes = Ingredientes.query.all()
        self.productos = Productos.query.all()
    
    def vender(self, name):
        try:
            producto = Productos.query.filter_by(nombre=name).first()
            
            
            if not producto:
                raise ValueError("Producto no encontrado")

            for ingrediente in producto.ingredientes:
                if ingrediente.inventario <= 0:
                    raise ValueError(f"!Oh no! Nos hemos quedado sin {ingrediente.nombre}")
            
            return "¡Vendido!"
    
        except ValueError as e:
            return str(e)