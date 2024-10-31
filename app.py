 
from flask import Flask, request, redirect, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv # Import dotenv to handle environment variables
import os
import string
import random
# Load environment variables from the .env file
load_dotenv()
# Create the Flask application
app = Flask(__name__)
# Configure the connection to MongoDB using the URI from the .env file
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.url_shortener
collection = db.urls
# Function to generate a short ID of given length (6 by default)
def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits # Uppercase letters, lowercase letters and digits.
    return ''.join(random.choice(characters) for _ in range(length))
# Start path: Render the main page with the URL form
@app.route('/')
def index():
    return render_template('index.html') # Load HTML file for interface.
# Endpoint to shorten the URL (POST method)
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json() # Get JSON data from request.
    original_url = data.get("url") # Extract the original URL
    # Check if the URL already exists in the database
    existing_url = collection.find_one({"original_url": original_url})
    if existing_url:
        # Return existing shortened URL if already generated.
        return jsonify({"short_url": request.host_url + existing_url["short_id"]})
    
    # Generate a short unique ID
    short_id = generate_short_id()
    while collection.find_one({"short_id": short_id}): # Ensure ID is unique
        short_id = generate_short_id()
    
    # Insert the original URL and the short ID into the database
    collection.insert_one({"short_id": short_id, "original_url": original_url})
    short_url = request.host_url + short_id # Create the complete shortened URL
    return jsonify({"short_url": short_url})
# Endpoint to redirect to the original URL using the short_id
@app.route('/<short_id>')
def redirect_url(short_id):
    # Search for the short ID in the database.
    url_data = collection.find_one({"short_id": short_id})
    if url_data:
        return redirect(url_data["original_url"]) # Redirect to the original URL.
    else:
        return jsonify({"error": "URL not found"}), 404 # Return error if doesn't exist.
# Start application in debug mode
if __name__ == '__main__':
    app.run(debug=True)



