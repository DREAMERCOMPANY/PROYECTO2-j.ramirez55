
from flask import Blueprint, render_template, request
from app import db
from app.models import Ingrediente, Producto, ProductoIngrediente

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
    producto = Producto.query.get_or_404(id)  
    esSano = True

    for ingrediente in producto.ingredientes:  
        if ingrediente.es_vegetariano == 0:
            esSano = False
            break  

    if esSano:
        return render_template('ingrediente_sano.html', producto=producto)
    else:
        return render_template('ingrediente_no_sano.html', producto=producto)

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
    calories = 0
    for ingrediente in producto.ingredientes:
        calories += ingrediente.calorias
    totalCalories = calories * 0.95
    return render_template('producto_calorias.html', producto=producto ,  totalCalories=totalCalories)



# Consultar rentabilidad de un producto por ID
@api.route('/producto/<int:id>/rentabilidad', methods=['GET'])
def show_producto_rentabilidad(id):
    producto = Producto.query.get_or_404(id)
    costo = 0
    for ingrediente in producto.ingredientes:
        costo += ingrediente.precio
    rentabilidad = producto.precio_publico - costo
    return render_template('producto_rentabilidad.html', producto=producto, rentabilidad=rentabilidad)

# Consultar costo de producción de un producto por ID
@api.route('/producto/<int:id>/costo_produccion', methods=['GET'])
def show_producto_costo_produccion(id):
    producto = Producto.query.get_or_404(id)
    costo = 0
    for ingrediente in producto.ingredientes:
        costo += ingrediente.precio
    return render_template('producto_costo_produccion.html', producto=producto, costo=costo)

# Vender un producto por ID
@api.route('/producto/<int:id>/vender', methods=['POST', 'GET'])
def vender_producto(id):
    producto = Producto.query.get_or_404(id)

    isInInvetario = True
    for ingrediente in producto.ingredientes:
        if ingrediente.inventario< 1:
            isInInvetario = False
            return render_template('producto_fuera_de_stock.html', ingrediente = ingrediente, producto= producto), 400
            
    
    if isInInvetario == True:
        for ingrediente in producto.ingredientes:
            ingrediente.inventario -= 1
        db.session.commit()
        return render_template('producto_vendido.html', producto=producto), 200
    
        
# Reabastecer un producto por ID
@api.route('/producto/<int:id>/reabastecer', methods=['POST'])
def reabastecer_producto(id):
    producto = Producto.query.get_or_404(id)
    cantidad = int(request.form.get('cantidad', 0))  # Obtener la cantidad del formulario
    
    # Reabastecer los ingredientes
    for ingrediente in producto.ingredientes:
        ingrediente.inventario += cantidad
    
    db.session.commit()
    
    return render_template('producto_reabastecido.html', producto=producto, cantidad=cantidad), 200





# Renovar inventario de un producto por ID
@api.route('/producto/<int:id>/renovar', methods=['POST'])
def renovar_producto(id):
    producto = Producto.query.get_or_404(id)
    cantidad = int(request.form.get('cantidad', 0))  # Obtener la cantidad del formulario
    
    # Reabastecer los ingredientes
    for ingrediente in producto.ingredientes:
        ingrediente.inventario = cantidad
    
    db.session.commit()
    
    return render_template('producto_renovado.html', producto=producto, cantidad=cantidad), 200

