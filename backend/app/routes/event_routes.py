from flask import Blueprint, request, jsonify
from app import db
from app.models import Event
from flask_jwt_extended import jwt_required, get_jwt_identity

event_routes = Blueprint('event_routes', __name__)

@event_routes.route('/events', methods=['POST'])
@jwt_required()
def create_event():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_event = Event(
        title=data['title'],
        description=data['description'],
        date_time=data['date_time'],
        location=data['location'],
        user_id=current_user['id']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created'}), 201

@event_routes.route('/events', methods=['GET'])
@jwt_required()
def list_events():
    events = Event.query.all()
    events_list = [{'id': e.id, 'title': e.title, 'date_time': e.date_time, 'location': e.location} for e in events]
    return jsonify(events_list), 200

@event_routes.route('/events/<int:id>', methods=['GET'])
@jwt_required()
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify({'title': event.title, 'description': event.description, 'date_time': event.date_time, 'location': event.location}), 200

@event_routes.route('/events/<int:id>', methods=['PUT'])
@jwt_required()
def update_event(id):
    data = request.get_json()
    event = Event.query.get_or_404(id)
    event.title = data['title']
    event.description = data['description']
    event.date_time = data['date_time']
    event.location = data['location']
    db.session.commit()
    return jsonify({'message': 'Event updated'}), 200

@event_routes.route('/events/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted'}), 200
