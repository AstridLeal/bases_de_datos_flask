from flask import Blueprint, jsonify
from models import User
from database import db

# Crea el Blueprint
routes = Blueprint('routes', __name__)

@routes.route('/add_user/<name>/<email>', methods=['GET'])
def add_user(name, email):
    try:
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": f"Usuario {name} agregado con éxito"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@routes.route('/usuarios', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify({"usuarios": [user.to_dict() for user in users]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
