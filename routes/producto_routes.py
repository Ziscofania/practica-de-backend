from flask import Blueprint
from controllers.producto_controller import obtener_productos

producto_bp = Blueprint('producto_bp', __name__)

# Ruta: /api/productos
@producto_bp.route('/api/productos', methods=['GET'])
def listar_productos():
    return obtener_productos()
