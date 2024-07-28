""" from flask import Blueprint, jsonify, request
from app import db
from app.models import Ingrediente, Producto, ProductoIngrediente

api = Blueprint('api', __name__)

   
@api.route('/ingredientes', methods=['GET'])
def get_ingredientes():
    ingredientes = Ingrediente.query.all()
    return jsonify([ingrediente.to_dict() for ingrediente in ingredientes])

@api.route('/ingrediente/<int:id>', methods=['GET'])
def get_ingrediente(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    return jsonify(ingrediente.to_dict())

@api.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([producto.to_dict() for producto in productos])

@api.route('/producto/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(producto.to_dict())

@api.route('/productos_ingredientes', methods=['GET'])
def get_productos_ingredientes():
    productos_ingredientes = ProductoIngrediente.query.all()
    return jsonify([producto_ingrediente.to_dict() for producto_ingrediente in productos_ingredientes])

@api.route('/producto_ingrediente/<int:id>', methods=['GET'])
def get_producto_ingrediente(id):
    producto_ingrediente = ProductoIngrediente.query.get_or_404(id)
    return jsonify(producto_ingrediente.to_dict()) """


""" from flask import Blueprint, jsonify, request
from app import db
from app.models import Ingrediente, Producto, ProductoIngrediente

api = Blueprint('api', __name__)

# Consultar todos los ingredientes
@api.route('/ingredientes', methods=['GET'], endpoint='get_ingredientes')
def get_ingredientes():
    ingredientes = Ingrediente.query.all()
    return jsonify([ingrediente.to_dict() for ingrediente in ingredientes])

# Consultar un ingrediente por ID
@api.route('/ingrediente/<int:id>', methods=['GET'], endpoint='get_ingrediente')
def get_ingrediente(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    return jsonify(ingrediente.to_dict())

# Consultar un ingrediente por nombre (si es necesario)
@api.route('/ingrediente/nombre/<string:nombre>', methods=['GET'], endpoint='get_ingrediente_por_nombre')
def get_ingrediente_por_nombre(nombre):
    ingrediente = Ingrediente.query.filter_by(nombre=nombre).first_or_404()
    return jsonify(ingrediente.to_dict())

# Consultar si un ingrediente es sano por ID
@api.route('/ingrediente/<int:id>/sano', methods=['GET'], endpoint='get_ingrediente_sano')
def get_ingrediente_sano(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    # Asumimos que existe un atributo `es_sano` en el modelo Ingrediente
    return jsonify(es_sano=ingrediente.es_sano)

# Consultar todos los productos
@api.route('/productos', methods=['GET'], endpoint='get_productos')
def get_productos():
    productos = Producto.query.all()
    return jsonify([producto.to_dict() for producto in productos])

# Consultar un producto por ID
@api.route('/producto/<int:id>', methods=['GET'], endpoint='get_producto')
def get_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(producto.to_dict())

# Consultar un producto por nombre
@api.route('/producto/nombre/<string:nombre>', methods=['GET'], endpoint='get_producto_por_nombre')
def get_producto_por_nombre(nombre):
    producto = Producto.query.filter_by(nombre=nombre).first_or_404()
    return jsonify(producto.to_dict())

# Consultar calorías de un producto por ID
@api.route('/producto/<int:id>/calorias', methods=['GET'], endpoint='get_producto_calorias')
def get_producto_calorias(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(calorias=producto.calorias)

# Consultar rentabilidad de un producto por ID
@api.route('/producto/<int:id>/rentabilidad', methods=['GET'], endpoint='get_producto_rentabilidad')
def get_producto_rentabilidad(id):
    producto = Producto.query.get_or_404(id)
    rentabilidad = producto.precio_publico - producto.costo_produccion
    return jsonify(rentabilidad=rentabilidad)

# Consultar costo de producción de un producto por ID
@api.route('/producto/<int:id>/costo_produccion', methods=['GET'], endpoint='get_producto_costo_produccion')
def get_producto_costo_produccion(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(costo_produccion=producto.costo_produccion)

# Vender un producto por ID
@api.route('/producto/<int:id>/vender', methods=['POST'], endpoint='vender_producto')
def vender_producto(id):
    producto = Producto.query.get_or_404(id)
    if producto.inventario > 0:
        producto.inventario -= 1
        db.session.commit()
        return jsonify(message='Producto vendido'), 200
    else:
        return jsonify(message='Producto fuera de stock'), 400

# Reabastecer un producto por ID
@api.route('/producto/<int:id>/reabastecer', methods=['POST'], endpoint='reabastecer_producto')
def reabastecer_producto(id):
    producto = Producto.query.get_or_404(id)
    cantidad = request.json.get('cantidad', 0)
    producto.inventario += cantidad
    db.session.commit()
    return jsonify(message='Producto reabastecido'), 200

# Renovar inventario de un producto por ID
@api.route('/producto/<int:id>/renovar', methods=['POST'], endpoint='renovar_producto')
def renovar_producto(id):
    producto = Producto.query.get_or_404(id)
    producto.inventario = request.json.get('nuevo_inventario', 0)
    db.session.commit()
    return jsonify(message='Inventario renovado'), 200 """

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

