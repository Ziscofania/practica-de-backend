# 🛠️ API REST de Inventario - Flask

Este proyecto es una API REST básica para la gestión de productos en un inventario, desarrollada con **Python** y **Flask**, estructurada de forma profesional para mostrar buenas prácticas de backend. 

Tecnologías Usadas

    Python 3.10+

    Flask

    Flask-CORS

    Postman (para pruebas)

Rutas Disponibles
 
**GET /**

Ruta raíz para comprobar que el servidor funciona.

**Respuesta:**
```bash
{
  "mensaje": "API Inventario corriendo correctamente 🛒"
}
```
**GET /api/productos**

Devuelve todos los productos almacenados en la base de datos simulada.

**Respuesta:**
```bash
{
  "productos": [
    {
      "id": 1,
      "nombre": "Mouse Gamer",
      "precio": 70000
    },
    {
      "id": 2,
      "nombre": "Teclado Mecánico",
      "precio": 120000
    },
    {
      "id": 3,
      "nombre": "Pantalla 24\"",
      "precio": 350000
    }
  ]
}
```

# Instalación y Ejecución
```bash
# 1. Clona el repositorio
git clone https://github.com/Ziscofania/practica-de-backend.git
cd inventario_api

# 2. Crea el entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Ejecuta el servidor
python app.py
```