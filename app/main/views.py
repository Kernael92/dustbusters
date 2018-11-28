from flask import Flask
from flask import render_template,redirect,url_for,abort
from . import main

@main.route('/')
def index():
    title='Home-Mama Safi'

    return render_template('index.html',title=title)

if __name__=='__main__':
    app.run()


