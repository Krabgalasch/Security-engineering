from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Security Misconfiguration: Debug mode enabled
app.config["DEBUG"] = True

# Data store for Unrestricted Resource Consumption
data_store = []

# Unrestricted Resource Consumption: No limits on data size or validations
@app.route('/store', methods=['POST'])
def store_data():
    data = request.json
    data_store.append(data)
    return jsonify({"status": "Data stored", "current_store_size": len(data_store)}), 200

# Unsafe Consumption of APIs: Consuming external APIs without validation
@app.route('/fetch', methods=['POST'])
def fetch_data():
    url = request.json.get("url")
    response = requests.get(url)  # No validation of the provided URL
    return jsonify({"content": response.text}), 200

# Server-Side Request Forgery (SSRF): Allowing the server to fetch attacker-controlled URLs
@app.route('/ssrf', methods=['POST'])
def ssrf():
    target_url = request.json.get("target_url")
    response = requests.get(target_url)  # Vulnerable to SSRF
    return jsonify({"status": "Request successful", "content": response.text}), 200

if __name__ == '__main__':
    # Security Misconfiguration: Exposing the server to public access
    app.run(host='0.0.0.0', port=5000)