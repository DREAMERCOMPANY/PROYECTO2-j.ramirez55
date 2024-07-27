from flask import Blueprint, jsonify, request
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
    return jsonify(producto_ingrediente.to_dict())
