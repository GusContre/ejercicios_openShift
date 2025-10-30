# app_a.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def call_app_b():
    try:
        # Llamamos a la app B, que está en localhost:3001
        response = requests.get('http://mi-servicio-microservicio-2.guscontre-dev.svc.cluster.local:4000/')
        return f'Respuesta de app B: {response.text}', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500


@app.route('/startup', methods=['GET'])
def startup_probe():
    return 'startup ok', 200


@app.route('/readiness', methods=['GET'])
def readiness_probe():
    # En producción podríamos validar dependencias externas antes de responder.
    return 'readiness ok', 200


@app.route('/health', methods=['GET'])
def liveness_probe():
    return 'health ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
