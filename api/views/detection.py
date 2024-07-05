from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models import Detection, db

detection_blueprint = Blueprint('detection', __name__)

@detection_blueprint.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    user_identity = get_jwt_identity()
    # Assume the code file is uploaded and processed here
    file_path = "path_to_uploaded_file"
    new_detection = Detection(user_id=user_identity, file_path=file_path)
    db.session.add(new_detection)
    db.session.commit()
    return jsonify({"msg": "File uploaded successfully"}), 200


@detection_blueprint.route('/api/results', methods=['GET'])
@jwt_required()
def results():
    user_identity = get_jwt_identity()
    detections = Detection.query.filter_by(user_id=user_identity).all()
    results = [{"id": d.id, "file_path": d.file_path, "result": d.result, "timestamp": d.timestamp} for d in detections]
    return jsonify(results), 200
