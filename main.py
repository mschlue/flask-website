import os
from flask import Flask, render_template, request, redirect, url_for, send_file

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
    return render_template('/resume/index.html')


@app.route('/seniordesign/')
def seniordesign():
    """Render the senior design page."""
    return render_template('seniordesign/index.html')


@app.route('/about/')
def about():
    """Render the about site page."""
    return render_template('about/index.html')


@app.route('/favicon.ico')
def favicon():
    """Render the website's contact page."""
    return send_file('static/img/favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')

