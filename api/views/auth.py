from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity, create_refresh_token
)
from api.models import User, _hash
import datetime
from api import db


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400
    print("He is registering", username, " ", email, "", password)

    # hashed_password = generate_password_hash(password)
    new_user = User(username=username,email=email, rank=2, password=_hash(password), plain_pass=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "status": "0",
        "msg": "User registered successfully"}), 200


@auth_blueprint.route('/api/login2', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print("He is login", f"{username} {password}")

    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return jsonify({
            "status":1,
            "msg": "Bad username or password"}), 401


    access_token = create_access_token(identity=user.id, fresh=3600)
    return jsonify({"user_id": user.id, "username": user.username,
                    "rank": user.rank, "access_token": access_token}), 200

@auth_blueprint.route('/upadteUserinfo', methods=['POST'])
def update_userinfo():
    data = request.form
    username = data.get('username')
    region = data.get('region')

    # user = User.query.filter_by(username=username).first()
    #
    # if not user:
    #     return jsonify({'error': 'User not found'}), 404
    #
    # if region:
    #     user.region = region
    # if avatar:
    #     user.avatar = avatar

    # db.session.commit()

    print("He is updating userinfo")
    return jsonify({'message': 'User information updated successfully'}), 200


@auth_blueprint.route('/profile', methods=['get', 'post'])
@jwt_required(refresh=True)
def profile():
    user_id = request.get_json().get('user_id')
    current_user = get_jwt_identity()
    info = {"name": "Fond", "region": "China", "age": 20}

    return jsonify(info), 200
