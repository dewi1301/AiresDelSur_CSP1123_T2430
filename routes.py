from flask import render_template
from flask_login import login_required
from __init__ import app

"""
@app.route('/')
def landing_page():
    return render_template('landing_page.html', is_fixed_header=True, main_content_height='1000px')
"""
@app.route('/home')
@login_required
def home_page():
    return render_template('home.html', is_fixed_header=True, main_content_height='1000px')

@app.route('/base')
def base_page():
    return render_template('base.html', is_fixed_header=True, main_content_height='1000px') #Base.HTML Debug Stage

@app.route('/partner_airlines')
def partner_airlines_page():
    return render_template('partner_airlines.html', is_fixed_header=True, main_content_height='1000px') #Partner_Airlines.HTML Debug Stage

@app.route('/about_us')
def about_us_page():
    return render_template('about_us.html', is_fixed_header=True, main_content_height='400px') #About_Us.HTML Debug Stage
