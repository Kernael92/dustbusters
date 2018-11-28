from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_location

@main.route('/')
def location():
    '''
    View root page function that returns the location page and its data
    '''

    # Getting location
    address = get_location('address')
    subAddress = get_location('subAddress')
    street_address = get_location('street_address')
    street_name = get_location('street_name')



    
    title = 'live location'



    return render_template('location.html', title = title, address=address, subAddress=subAddress,street_name=street_name,street_address=street_address)



    