from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def serve_data():
    if not os.path.exists('scraped_data.json'):
        return jsonify({"title":"Devops assignment done successfully!!","heading":"Devops"}), 404

    with open('scraped_data.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
