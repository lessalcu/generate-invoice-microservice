import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_mongo_client():
    """Gets the MongoDB collection configured in .env."""
    mongo_uri = os.getenv("MONGO_URI")
    mongo_db = os.getenv("MONGO_DB")
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    return db[os.getenv("MONGO_COLLECTION")]
