# Importación de Flask y jsonify
from flask import Flask, jsonify

app = Flask(__name__)

# Creación de lista aleatoria de autos
autos = [
    {"marca": "Toyota", "modelo": "Corolla", "año": 2022, "precio": 20000, "color": "Rojo"},
    {"marca": "Honda", "modelo": "Civic", "año": 2021, "precio": 22000, "color": "Azul"},
    {"marca": "Ford", "modelo": "Focus", "año": 2020, "precio": 18000, "color": "Negro"},
    {"marca": "Chevrolet", "modelo": "Malibu", "año": 2019, "precio": 17000, "color": "Blanco"},
    {"marca": "Nissan", "modelo": "Sentra", "año": 2023, "precio": 21000, "color": "Gris"}
]

# Ruta para obtener el catálogo de autos
@app.route('/autos', methods=['GET'])
def obtener_autos():
    return jsonify(autos)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
