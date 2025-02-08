from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize MongoDB extension
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/InvoiceDB")
    
    # Initialize MongoDB connection
    mongo.init_app(app)

    # Register the blueprint
    from app.controllers.invoice_controller import invoice_bp
    app.register_blueprint(invoice_bp)
    
    return app
