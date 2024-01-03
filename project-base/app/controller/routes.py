from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('services.html')

@app.route('/work-single')
def workSingle():
    return render_template('work-single.html')

@app.route('/works')
def works():
    return render_template('works.html')

