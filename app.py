from flask import Flask
from app import create_app

if __name__ == '__main__':
    app = Flask(__name__)
    create_app(app)



