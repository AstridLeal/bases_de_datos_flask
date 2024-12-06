from flask import Flask
from database import db
from routes import routes
    
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mazapan2022%21@localhost:5432/mi_flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos
db.init_app(app)

# Registra el Blueprint
app.register_blueprint(routes)

# Crear tablas en la base de datos si no existen
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)