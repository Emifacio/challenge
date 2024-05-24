import logging
from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_jwt_extended import create_access_token

user_routes = Blueprint('user_routes', __name__)

logging.basicConfig(level=logging.DEBUG)

@user_routes.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data or not data.get('username') or not data.get('email') or not data.get('password'):
            logging.error('Missing data')
            return jsonify({'message': 'Missing data'}), 400

        if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
            logging.error('User already exists')
            return jsonify({'message': 'User already exists'}), 400

        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        logging.info('User registered successfully')
        return jsonify({'message': 'User registered'}), 201
    except Exception as e:
        logging.error(f'Error: {e}')
        return jsonify({'message': 'Internal server error'}), 500


@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.verify_password(data['password']):
        access_token = create_access_token(identity={'username': user.username, 'email': user.email})
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401