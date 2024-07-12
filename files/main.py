from base import Base
from complemento import Complemento
from copa import Copa
from malteada import Malteada
from heladeria import Heladeria

# Crear ingredientes
base_fresa = Base(precio=2.0, calorias=50, nombre="Base de Fresa", es_vegetariano=True, sabor="Fresa")
complemento_chocolate = Complemento(precio=1.0, calorias=100, nombre="Chocolate", es_vegetariano=True)
complemento_nueces = Complemento(precio=1.5, calorias=150, nombre="Nueces", es_vegetariano=True)
complemento_menta = Complemento(precio=1.2, calorias=80, nombre="Menta", es_vegetariano=True)

# Abastecer inventarios
base_fresa.abastecer()
complemento_chocolate.abastecer()
complemento_nueces.abastecer()
complemento_menta.abastecer()

# Mostrar inventarios después de abastecer
print(f"Inventario Base Fresa: {base_fresa.get_inventario()}")
print(f"Inventario Chocolate: {complemento_chocolate.get_inventario()}")
print(f"Inventario Nueces: {complemento_nueces.get_inventario()}")
print(f"Inventario Menta: {complemento_menta.get_inventario()}")

# Crear productos
copa_fresa = Copa(nombre="Copa de Fresa", precio_publico=5.0, ingrediente1=base_fresa, ingrediente2=complemento_chocolate, ingrediente3=complemento_nueces, tipo_vaso="Vaso pequeño")
malteada_menta = Malteada(nombre="Malteada de Menta", precio_publico=6.0, ingrediente1=base_fresa, ingrediente2=complemento_menta, ingrediente3=complemento_chocolate, volumen=0.5)

# Crear heladería
heladeria = Heladeria(producto1=copa_fresa, producto2=malteada_menta, producto3=copa_fresa, producto4=malteada_menta)

# Añadir ingredientes a la heladería
heladeria.add_ingrediente(base_fresa)
heladeria.add_ingrediente(complemento_chocolate)
heladeria.add_ingrediente(complemento_nueces)
heladeria.add_ingrediente(complemento_menta)

# Mostrar ingredientes añadidos a la heladería
print(f"Ingredientes en la heladería: {[ingrediente.get_nombre() for ingrediente in heladeria.get_ingredientes()]}")

# Llamar métodos de los productos
print(f"Calorías de Copa de Fresa: {copa_fresa.calcular_calorias()}")
print(f"Costo de Copa de Fresa: {copa_fresa.calcular_costo()}")
print(f"Rentabilidad de Copa de Fresa: {copa_fresa.calcular_rentabilidad()}")

print(f"Calorías de Malteada de Menta: {malteada_menta.calcular_calorias()}")
print(f"Costo de Malteada de Menta: {malteada_menta.calcular_costo()}")
print(f"Rentabilidad de Malteada de Menta: {malteada_menta.calcular_rentabilidad()}")

# Mostrar atributos de los productos
print(f"Tipo de vaso de Copa de Fresa: {copa_fresa.get_tipoVaso()}")
print(f"Volumen de Malteada de Menta: {malteada_menta.get_volumen()}")

# Vender productos
heladeria.vender("Copa de Fresa")
heladeria.vender("Malteada de Menta")

# Mostrar inventarios después de la venta
print(f"Inventario Base Fresa después de ventas: {base_fresa.get_inventario()}")
print(f"Inventario Chocolate después de ventas: {complemento_chocolate.get_inventario()}")
print(f"Inventario Nueces después de ventas: {complemento_nueces.get_inventario()}")
print(f"Inventario Menta después de ventas: {complemento_menta.get_inventario()}")

# Utilizar métodos de Ingrediente
print(f"Base Fresa es sano: {base_fresa.es_sano()}")
base_fresa.set_sabor("Vainilla")
print(f"Nuevo sabor de Base Fresa: {base_fresa.get_sabor()}")

# Abastecer más ingredientes
base_fresa.abastecer()
complemento_chocolate.abastecer()
print(f"Inventario Base Fresa después de reabastecer: {base_fresa.get_inventario()}")
print(f"Inventario Chocolate después de reabastecer: {complemento_chocolate.get_inventario()}")
