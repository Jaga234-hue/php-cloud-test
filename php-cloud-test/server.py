from flask import Flask, jsonify
from flask_cors import CORS  # Install with: pip install flask-cors

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/')
def home():
    return jsonify({"message": "Server is running!"})

@app.route('/api/test', methods=['GET', 'POST'])
def test_endpoint():
    return jsonify({"status": "success", "data": "Hello from Render!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
