import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def get_mongo_client():
    """Obtiene la colección de MongoDB configurada en .env."""
    mongo_uri = os.getenv("MONGO_URI")
    mongo_db = os.getenv("MONGO_DB")
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    return db[os.getenv("MONGO_COLLECTION")]
