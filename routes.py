from flask import render_template, request, flash, redirect, url_for
from app import app
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    """Homepage with hero section and company introduction"""
    return render_template("index.html")

@app.route("/services")
def services():
    """Services page showcasing IT consulting offerings"""
    return render_template("services.html")

@app.route("/partners")
def partners():
    """Partners page displaying business partnerships"""
    return render_template("partners.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact page with contact form and business information"""
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Basic validation
        if not name or not email or not message:
            flash("Please fill in all required fields.", "error")
            return redirect(url_for("contact"))
        
        # In a real application, you would save this to a database
        # or send an email. For now, we'll just show a success message
        flash(f"Thank you {name}! Your message has been received. We'll get back to you soon.", "success")
        app.logger.info(f"Contact form submitted by {name} ({email}): {message}")
        
        return redirect(url_for("contact"))
    
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template("500.html"), 500
