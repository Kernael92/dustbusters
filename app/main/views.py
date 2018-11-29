from flask import Flask
from flask import render_template,redirect,url_for,abort
from . import main

@main.route('/')
def index():
    title='Home-Clean club'

    return render_template('index.html',title=title)

@main.route('/about')
def about():
    title='About Us- Clean club'
    return render_template('about.html',title=title)



