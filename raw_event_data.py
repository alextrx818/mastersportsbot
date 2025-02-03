import sys
import os
import json
from flask import Flask, jsonify, request
import requests
from src.betsapi.auth.config import BetsAPIConfig

app = Flask(__name__)

def get_raw_event_data(event_id, event_type='inplay'):
    """Get raw event data from BetsAPI endpoints
    
    Args:
        event_id: The event ID to fetch
        event_type: Either 'inplay' or 'prematch'
    """
    config = BetsAPIConfig()
    
    if event_type == 'prematch':
        url = f"https://api.b365api.com/v3/bet365/prematch?token={config.TOKEN}&FI={event_id}&raw=1"
    else:
        url = f"https://api.b365api.com/v1/bet365/inplay?token={config.TOKEN}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # For inplay events, filter for specific event
        if event_type == 'inplay' and event_id:
            if 'success' in data and data['success'] == 1 and 'results' in data:
                events = data['results'][0]
                for event in events:
                    if event.get('type') == 'EV' and str(event.get('OI', '')) == str(event_id):
                        return {"success": 1, "results": [event]}
                return {"success": 0, "error": f"Event ID {event_id} not found"}
            else:
                return {"success": 0, "error": "No results in API response"}
        
        return data
    except requests.exceptions.RequestException as e:
        return {"success": 0, "error": str(e)}

@app.route('/')
def get_all_events():
    """Get all inplay events"""
    data = get_raw_event_data(None)
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/event/<event_id>')
def get_event(event_id):
    """Get specific event by ID"""
    event_type = request.args.get('type', 'inplay')  # Default to inplay if not specified
    data = get_raw_event_data(event_id, event_type)
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    # Add the project root to Python path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    app.run(debug=True, port=5001)
