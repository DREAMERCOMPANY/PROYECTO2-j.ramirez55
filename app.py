from app import create_app
from config import Config
app = create_app(Config)
print("Application created successfully")

if __name__ == '__main__':
    app.run()
