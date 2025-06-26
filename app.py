from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        result = subprocess.run(
            ['python3', 'predict.py', message],
            capture_output=True,
            text=True,
            check=True
        )
        output = json.loads(result.stdout.strip())
        return jsonify(output)

    except subprocess.CalledProcessError as e:
        return jsonify({
            'error': 'Python script error',
            'details': e.stderr
        }), 500

    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON from predict.py'}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
