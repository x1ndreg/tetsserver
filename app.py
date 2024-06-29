from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, allowing cross-origin requests

# Dictionary to store user locations, keyed by user_id
user_locations = {}

# Route for root URL
@app.route('/')
def index():
    return "Welcome to my Flask server!"

# Route for updating location
@app.route('/update_location', methods=['POST'])
def update_location():
    if request.method == 'POST':
        data = request.get_json()
        print('Received data:', data)
        user_id = data.get('user_id')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        print(f"User ID: {user_id}, Latitude: {latitude}, Longitude: {longitude}")
        
        # Store the location data
        if user_id and latitude is not None and longitude is not None:
            user_locations[user_id] = {'latitude': latitude, 'longitude': longitude}
        
        # Return a response to the Flutter app
        return jsonify({'message': 'Location updated successfully'}), 200
    
    return jsonify({'message': 'Method not allowed'}), 405

# Route to get all user locations
@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify(user_locations), 200

# Route to serve map page
@app.route('/map')
def show_map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
