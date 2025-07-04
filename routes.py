from flask import render_template, request, flash, redirect, url_for, session
from app import app, get_locale
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    """Homepage with hero section and company introduction"""
    current_lang = get_locale()
    return render_template("index.html", lang=current_lang)

@app.route("/set_language/<language>")
def set_language(language):
    """Set the language preference"""
    if language in app.config['LANGUAGES']:
        session['language'] = language
    return redirect(request.referrer or url_for('index'))

@app.route("/services")
def services():
    """Services page showcasing IT consulting offerings"""
    current_lang = get_locale()
    return render_template("services.html", lang=current_lang)

@app.route("/partners")
def partners():
    """Partners page displaying business partnerships"""
    current_lang = get_locale()
    return render_template("partners.html", lang=current_lang)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact page with contact form and business information"""
    current_lang = get_locale()
    
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Basic validation
        if not name or not email or not message:
            if current_lang == 'fr':
                flash("Veuillez remplir tous les champs obligatoires.", "error")
            else:
                flash("Please fill in all required fields.", "error")
            return redirect(url_for("contact"))
        
        # In a real application, you would save this to a database
        # or send an email. For now, we'll just show a success message
        if current_lang == 'fr':
            flash(f"Merci {name}! Votre message a été reçu. Nous vous répondrons bientôt.", "success")
        else:
            flash(f"Thank you {name}! Your message has been received. We'll get back to you soon.", "success")
        app.logger.info(f"Contact form submitted by {name} ({email}): {message}")
        
        return redirect(url_for("contact"))
    
    return render_template("contact.html", lang=current_lang)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template("500.html"), 500
