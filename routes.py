from app import app, db
from models import Usuario
from flask import render_template, redirect, url_for

# Ruta para agregar un nuevo usuario
@app.route('/add_user/<nombre>/<email>')
def add_user(nombre, email):
    # Creamos un nuevo usuario con los datos proporcionados
    usuario = Usuario(nombre=nombre, email=email)
    
    # Lo agregamos a la sesión de la base de datos
    db.session.add(usuario)
    db.session.commit()  # Confirmamos los cambios

    # Mensaje de éxito
    return f'Usuario {nombre} agregado con éxito.'

# Ruta para mostrar todos los usuarios
@app.route('/usuarios')
def usuarios():
    # Consultamos todos los usuarios en la base de datos
    usuarios = Usuario.query.all()

    # Los mostramos en formato HTML simple
    return '<br>'.join([f'{u.id}. {u.nombre} - {u.email}' for u in usuarios])
