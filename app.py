""" from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# Inicialización de la extensión SQLAlchemy
db = SQLAlchemy(app)

# Definición de modelos
class Ingredientes(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Float, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)

    def es_sano(self):
        return self.calorias < 200 and self.es_vegetariano

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    ingredientes = db.relationship('Ingredientes', secondary = 'productos_ingredientes' , backref=db.backref('productos', lazy='dynamic'))

class ProductosIngredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingredientes.ID'), nullable=False)

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

# Rutas de la aplicación Flask
@app.route('/')
def index():
    productos = Productos.query.all()
    return render_template('index.html', productos=productos)

@app.route('/ingredientes')
def mostrar_ingredientes():
    heladeria = Heladeria()
    ingredientes = heladeria.ingredientes
    return render_template('ingredientes.html', ingredientes=ingredientes) 

@app.route('/vender/<productName>' )
def vender_producto(productName):
        #return 'Hello'
        heladeria = Heladeria()
        resultado = heladeria.vender(productName)  
        return resultado 
     """
from db import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# Inicialización de la extensión SQLAlchemy
db.init_app(app)
import controllers.controller

if __name__ == '__app__':
    app.run(debug=True) 


