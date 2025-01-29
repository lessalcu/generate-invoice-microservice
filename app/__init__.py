from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Inicializar la extensión de MongoDB
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/InvoiceDB")
    
    # Inicializar la conexión con MongoDB
    mongo.init_app(app)

    # Registrar el blueprint
    from app.controllers.invoice_controller import invoice_bp
    app.register_blueprint(invoice_bp, url_prefix="/api/invoice")
    
    return app
