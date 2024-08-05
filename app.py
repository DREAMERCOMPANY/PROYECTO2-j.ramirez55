from app import create_app
app = create_app()
print("Application created successfully")

if __name__ == '__main__':
    app.run()
