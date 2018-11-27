import urllib.request,json
from .models import Location


# Getting the location base url
base_url = None
# Getting the client Id
client_id = None
# Getting the client secret
client_secret = None
# Getting temporary token
temporary_token = None

def configure_request(app):
    global base_url,client_id,client_secret,temporary_token
    base_url = app.config['LOCATION_BASE_URL']
    client_id = app.config['CLIENT_ID']
    client_secret = app.config['CLIENT_SECRET']
    temporary_token = app.config['TEMPORARY_TOKEN']

def get_location(stName):
    '''
    Function that gets the json response to our url request
    '''
    get_locations_url = base_url.format(stName)
    with urllib.request.urlopen(get_locations_url) as url:
        get_locations_data = url.read()
        get_locations_response = json.loads(get_locations_data)

        location_results = None

        if get_locations_response['candidates']:
            location_results_list = get_locations_response['candidates']
            location_results = process_results(location_results_list)
    return location_results



