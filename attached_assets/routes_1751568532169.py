from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/partners")
def partners():
    return render_template("partners.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")