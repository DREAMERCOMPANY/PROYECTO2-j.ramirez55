from db import db
from models.ingredientes import Ingredientes
from models.productos_ingredientes import ProductosIngredientes

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    ingredientes = db.relationship('Ingredientes', secondary = 'productos_ingredientes' , backref=db.backref('productos', lazy='dynamic'))