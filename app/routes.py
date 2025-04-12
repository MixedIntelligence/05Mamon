# File: app/routes.py
# Path: app/
# Description: Contains API routes for logging composting activities and issuing tokens.

from flask import request, jsonify
from app import db
from app.models import User, CompostingLog

@app.route('/log-compost', methods=['POST'])
def log_compost():
    """
    Endpoint: Log composting activity.
    Accepts user_id and weight (in kg) as JSON input.
    Automatically issues tokens based on compost weight.
    """
    data = request.get_json()
    user_id = data.get('user_id')
    weight = data.get('weight')

    if not user_id or not weight:
        return jsonify({'error': 'Missing user_id or weight'}), 400

    # Create a new composting log entry
    compost_log = CompostingLog(user_id=user_id, weight=weight)
    db.session.add(compost_log)

    # Update user's token balance
    user = User.query.get(user_id)
    if user:
        user.tokens_balance += weight  # Issue 1 token per kg of compost
    else:
        return jsonify({'error': 'User not found'}), 404

    # Commit changes to the database
    db.session.commit()
    return jsonify({'message': 'Composting logged and tokens issued'}), 201
