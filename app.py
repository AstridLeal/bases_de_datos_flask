from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes import *  # Aquí va el import de routes

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Aquí va la creación de tablas antes de que se procese la primera solicitud
with app.app_context():     
    # Inicializamos la DB y creamos todas las tablas
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
