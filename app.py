from flask import Flask, request, redirect, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import os   
import string
import random

# Load environment variables from a .env file
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)

# Configure the connection to MongoDB using the connection string stored in the environment variable
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)  # Create a MongoClient instance to interact with MongoDB
db = client.url_shortener         # Access the 'url_shortener' database
collection = db.urls              # Access the 'urls' collection within the database

# Ensure index for automatic expiration
collection.create_index("created_at", expireAfterSeconds=2592000) 

# Function to generate a short ID for the URL
def generate_short_id(length=6):
    # Create a string of characters that includes letters and digits
    characters = string.ascii_letters + string.digits
    # Randomly select characters from the string to create a short ID of the specified length
    return ''.join(random.choice(characters) for _ in range(length))

# Route for the homepage
@app.route('/')
def index():
    # Render and return the 'index.html' template
    return render_template('index.html')

# Endpoint to shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        original_url = data.get("url")  # Extract the original URL

        # Check if original_url is provided
        if not original_url:
            return jsonify({"error": "No URL provided"}), 400

        existing_url = collection.find_one({"original_url": original_url})
        if existing_url:
            return jsonify({"short_url": request.host_url + existing_url["short_id"]})

        short_id = generate_short_id()
        while collection.find_one({"short_id": short_id}):
            short_id = generate_short_id()

        collection.insert_one({
            "short_id": short_id,
            "original_url": original_url,
            "created_at": datetime.utcnow()  # UTC timestamp
        })
        short_url = request.host_url + short_id
        return jsonify({"short_url": short_url}), 201  # Return a 201 Created status

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error shortening URL: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500


# Endpoint to redirect to the original URL using the short ID
@app.route('/<short_id>')
def redirect_url(short_id):
    # Look for the original URL corresponding to the provided short ID
    url_data = collection.find_one({"short_id": short_id})
    if url_data:
        # If found, redirect to the original URL
        return redirect(url_data["original_url"])
    else:
        # If not found, return a 404 error with an error message
        return jsonify({"error": "URL not found"}), 404

# Función para eliminar enlaces caducados
def delete_expired_urls():
    try:
        # Calcula la fecha límite (30 días atrás)
        expiration_date = datetime.utcnow() - timedelta(days=30)
        # Elimina los documentos cuyo `created_at` sea menor a la fecha límite
        result = collection.delete_many({"created_at": {"$lt": expiration_date}})
        print(f"Deleted {result.deleted_count} expired URLs.")
    except Exception as e:
        print(f"Error deleting expired URLs: {e}")

# Configurar el programador para ejecutar la tarea periódicamente
scheduler = BackgroundScheduler()
scheduler.add_job(delete_expired_urls, 'interval', hours=24)  # Ejecuta cada 24 horas
scheduler.start()
