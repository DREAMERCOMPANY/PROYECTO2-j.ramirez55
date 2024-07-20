# Rutas de la aplicación Flask
from db import db
from models.productos import Productos
from models.heladeria import Heladeria
from app import app
from flask import render_template


@app.route('/')
def index():
    heladeria = Heladeria()
    productos = heladeria.productos
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
    