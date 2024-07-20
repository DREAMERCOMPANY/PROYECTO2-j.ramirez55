# Modelo de ingredientes
from db import db

class Ingredientes(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Float, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)

    def es_sano(self):
        return self.calorias < 200 and self.es_vegetariano