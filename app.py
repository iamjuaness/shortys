from flask import Flask, request, redirect, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
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
    # Get the JSON data from the request
    data = request.get_json()
    original_url = data.get("url")  # Extract the original URL from the request data

    # Check if the original URL already exists in the database
    existing_url = collection.find_one({"original_url": original_url})
    if existing_url:
        # If it exists, return the existing short URL
        return jsonify({"short_url": request.host_url + existing_url["short_id"]})

    # Generate a unique short ID
    short_id = generate_short_id()
    # Ensure that the generated short ID is unique in the collection
    while collection.find_one({"short_id": short_id}):
        short_id = generate_short_id()

    # Insert the new short URL mapping into the database
    collection.insert_one({"short_id": short_id, "original_url": original_url})
    short_url = request.host_url + short_id  # Construct the full short URL
    return jsonify({"short_url": short_url})  # Return the short URL as JSON response

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
