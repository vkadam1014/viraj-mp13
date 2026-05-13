"""
Premium Tier Flask API service.

This module provides a minimal Flask application that exposes an endpoint to launch
Kubernetes jobs in the 'premium-service' namespace.

Students should extend this code to add additional endpoints, error handling,
or business logic as required by the assignment.
"""

from kubernetes import client, config
from flask import Flask, request, jsonify
import yaml
import time
# Load Kubernetes configuration 
try:
    config.load_incluster_config() 
except config.config_exception.ConfigException:
    config.load_kube_config()  

# Initialize Flask app
v1 = client.CoreV1Api()
app = Flask(__name__)
batch_v1 = client.BatchV1Api()
core_v1 = client.CoreV1Api()

# TODO: Define a POST endpoint that:
#   - Parses the incoming JSON for the 'dataset' parameter
#   - Loads the job YAML template
#   - Injects the dataset value into the job spec
#   - Generates a unique job name
#   - Submits the job to the Kubernetes cluster
#   - Returns a success or error response
@app.route('/premium', methods=['POST'])
def post_premium():
    try:
        data = request.get_json() or {}
        dataset = data.get('dataset', "kmnist")  # Default to 'kmnist' if not provided
        with open("premium-tier-job.yaml", "r") as f:
            job_yaml = yaml.safe_load(f)
        job_name = f"premium-job-{dataset}-{int(time.time())}"
        job_yaml['metadata']['name'] = job_name
        job_yaml['metadata']['namespace'] = 'premium-service'
        container = job_yaml['spec']['template']['spec']['containers'][0]
        container['env'] = [
            {'name': 'DATASET', 'value': dataset},
            {'name': 'TYPE', 'value': 'cnn'}
        ]
        batch_v1.create_namespaced_job(namespace='premium-service', body=job_yaml)
        return jsonify({
            "status": "success",
            "job_name": job_name,
            "dataset": dataset
        }), 200
    except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)