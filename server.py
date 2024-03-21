from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    """
    Endpoint to get the list of location names.

    Returns:
    - JSON response containing the list of location names.
    """
    # Get location names using the utility function
    response = jsonify({
        'locations': util.get_location_names()
    })
    # Allow cross-origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    """
    Endpoint to predict the home price based on input parameters.

    Returns:
    - JSON response containing the estimated home price.
    """
    # Extract parameters from the request
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Predict home price using the utility function
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    # Allow cross-origin requests
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    # Start Flask server
    print("Starting Python Flask Server For Home Price Prediction...")
    # Load saved artifacts
    util.load_saved_artifacts()
    app.run()
