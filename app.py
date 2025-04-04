from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)
KLAVIYO_API_KEY = "pk_07a3dd7a50335ec9100f5da4ceb2bf8161"
BASE_URL = "https://api.klaviyo.com/api"

headers = {
    "Authorization": f"Klaviyo-API-Key {KLAVIYO_API_KEY}",
    "revision": "2023-10-15"
}

def klaviyo_get(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}/"
    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json()), response.status_code

@app.route("/metrics", methods=["GET"])
def get_metrics():
    return klaviyo_get("metrics")

@app.route("/profiles", methods=["GET"])
def get_profiles():
    return klaviyo_get("profiles")

@app.route("/campaigns", methods=["GET"])
def get_campaigns():
    return klaviyo_get("campaigns")

@app.route("/flows", methods=["GET"])
def get_flows():
    return klaviyo_get("flows")

@app.route("/deliverability", methods=["GET"])
def get_deliverability():
    return klaviyo_get("deliverability")

if __name__ == "__main__":
    app.run(debug=True)
