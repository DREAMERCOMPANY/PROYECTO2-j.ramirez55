from app.main import create_app
app = create_app()
print("Application created successfully")

if __name__ == '__main__':
    app.run()
