# app_a.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def call_app_b():
    try:
        # Llamamos a la app B, que está en localhost:3001
        response = requests.get('http://mi-servicio-2.guscontre-dev.svc.cluster.local:4000/')
        return f'Respuesta de app B: {response.text}', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)