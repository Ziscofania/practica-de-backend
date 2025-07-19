from flask import Flask
from flask_cors import CORS
from routes.producto_routes import producto_bp

app = Flask(__name__)
CORS(app)  # Permite conexiones desde otros orígenes (como Postman o una app web)

# Registrar rutas de productos
app.register_blueprint(producto_bp)

@app.route('/')
def home():
    return {'mensaje': 'API Inventario corriendo correctamente 🛒'}

if __name__ == '__main__':
    app.run(debug=True)
