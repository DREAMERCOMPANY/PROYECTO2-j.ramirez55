
from flask import Blueprint, render_template, request
from app import db
from app.models import Ingrediente, Producto

api = Blueprint('api', __name__)

# Consultar todos los ingredientes
@api.route('/ingredientes', methods=['GET'])
def show_ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template('ingredientes.html', ingredientes=ingredientes)

# Consultar un ingrediente por ID
@api.route('/ingrediente/<int:id>', methods=['GET'])
def show_ingrediente(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    return render_template('ingrediente.html', ingrediente=ingrediente)

# Consultar un ingrediente por nombre (si es necesario)
@api.route('/ingrediente/nombre/<string:nombre>', methods=['GET'])
def show_ingrediente_por_nombre(nombre):
    ingrediente = Ingrediente.query.filter_by(nombre=nombre).first_or_404()
    return render_template('ingrediente.html', ingrediente=ingrediente)

# Consultar si un ingrediente es sano por ID
@api.route('/ingrediente/<int:id>/sano', methods=['GET'])
def show_ingrediente_sano(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    return render_template('ingrediente_sano.html', ingrediente=ingrediente)

# Consultar todos los productos
@api.route('/productos', methods=['GET'])
def show_productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

# Consultar un producto por ID
@api.route('/producto/<int:id>', methods=['GET'])
def show_producto(id):
    producto = Producto.query.get_or_404(id)
    return render_template('producto.html', producto=producto)

# Consultar un producto por nombre
@api.route('/producto/nombre/<string:nombre>', methods=['GET'])
def show_producto_por_nombre(nombre):
    producto = Producto.query.filter_by(nombre=nombre).first_or_404()
    return render_template('producto.html', producto=producto)

# Consultar calorías de un producto por ID
@api.route('/producto/<int:id>/calorias', methods=['GET'])
def show_producto_calorias(id):
    producto = Producto.query.get_or_404(id)
    return render_template('producto_calorias.html', producto=producto)

# Consultar rentabilidad de un producto por ID
@api.route('/producto/<int:id>/rentabilidad', methods=['GET'])
def show_producto_rentabilidad(id):
    producto = Producto.query.get_or_404(id)
    rentabilidad = producto.precio_publico - producto.costo_produccion
    return render_template('producto_rentabilidad.html', producto=producto, rentabilidad=rentabilidad)

# Consultar costo de producción de un producto por ID
@api.route('/producto/<int:id>/costo_produccion', methods=['GET'])
def show_producto_costo_produccion(id):
    producto = Producto.query.get_or_404(id)
    return render_template('producto_costo_produccion.html', producto=producto)

# Vender un producto por ID
@api.route('/producto/<int:id>/vender', methods=['POST'])
def vender_producto(id):
    producto = Producto.query.get_or_404(id)
    if producto.inventario > 0:
        producto.inventario -= 1
        db.session.commit()
        return render_template('producto_vendido.html', producto=producto), 200
    else:
        return render_template('producto_fuera_de_stock.html', producto=producto), 400

# Reabastecer un producto por ID
@api.route('/producto/<int:id>/reabastecer', methods=['POST'])
def reabastecer_producto(id):
    producto = Producto.query.get_or_404(id)
    cantidad = request.json.get('cantidad', 0)
    producto.inventario += cantidad
    db.session.commit()
    return render_template('producto_reabastecido.html', producto=producto), 200

# Renovar inventario de un producto por ID
@api.route('/producto/<int:id>/renovar', methods=['POST'])
def renovar_producto(id):
    producto = Producto.query.get_or_404(id)
    producto.inventario = request.json.get('nuevo_inventario', 0)
    db.session.commit()
    return render_template('producto_renovado.html', producto=producto), 200

