from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    """
    Handle GET request to fetch sample data.
    Responds with a greeting message
    Returns: JSON
    """
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Perform a health check for the application.
    Responds with a health status message
    Returns: JSON
    """
    health = {"status": "healthy"}
    return jsonify(health)

if __name__ == '__main__':
    # Run the Flask application server on host 0.0.0.0 and port 1234
    app.run(host='0.0.0.0', port=1234)