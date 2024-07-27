from flask_login import UserMixin
from app.extensiones import bcrypt, db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    es_admin = db.Column(db.Boolean, default=False)
    es_empleado = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, default=False)
    inventario = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'calorias': self.calorias,
            'es_vegetariano': self.es_vegetariano,
            'inventario': self.inventario
        }

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), unique=True, nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio_publico': self.precio_publico
        }

class ProductoIngrediente(db.Model):
    __tablename__ = 'productos_ingredientes'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)

    producto = db.relationship('Producto', backref=db.backref('producto_ingredientes', lazy=True))
    ingrediente = db.relationship('Ingrediente', backref=db.backref('producto_ingredientes', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'producto_id': self.producto_id,
            'ingrediente_id': self.ingrediente_id
        }
