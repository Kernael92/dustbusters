from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_location

@main.route('/location/<stName>')
def location():
    '''
    View root page function that returns the location page and its data
    '''

    # Getting location


    location = get_location('stName')
    title = 'live location'
    


    return render_template('location.html',location = location, title = title)



    