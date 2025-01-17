from flask import Flask
from app.config import Config
from app.extensiones import db, migrate, login, bcrypt

def create_app(app, config_class=Config):
    app.config.from_object(config_class)

    print("Configuration Loaded:")
    for key, value in app.config.items():
        print(f"{key}: {value}")

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bcrypt.init_app(app)

    login.login_view = 'auth.login'
    login.login_message = 'Please log in to access this page.'

    from app.models import User  

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.auth import auth_bp
    from app.routes import api as api_blueprint

    app.register_blueprint(auth_bp)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app



if __name__ == '__main__':
    app = Flask(__name__)
    create_app(app)





