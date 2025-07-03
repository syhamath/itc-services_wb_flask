import os
from flask import Flask, request, session

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Configure supported languages
app.config['LANGUAGES'] = {
    'en': 'English',
    'fr': 'Français'
}

def get_locale():
    # 1. URL parameter has highest priority
    if request.args.get('lang'):
        session['language'] = request.args.get('lang')
    
    # 2. User session
    if 'language' in session:
        return session['language']
    
    # 3. Browser language preference or default to English
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys()) or 'en'

# Import routes after app creation to avoid circular imports
from routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
