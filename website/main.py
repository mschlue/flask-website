import os
from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'configured_before_deploy')


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')


@app.route('/home/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/resume/')
def resume():
    """Render the resume page."""
    return render_template('/resume.html')


@app.route('/seniordesign/')
def seniordesign():
    """Render the senior design page."""
    return render_template('seniordesign.html')


@app.route('/about/')
def about():
    """Render the about site page."""
    return render_template('about.html')


@app.route('/favicon.ico')
def favicon():
    """Render the website's contact page."""
    return send_file('static/img/favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


def run_server():
    app.run(host='0.0.0.0')

