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
            location_results = process_candidates(location_results_list)
    return location_results

def process_candidates(location_list):
    '''
    Function that processes the location result and transform them to a list of objects
    '''
    location_results = []
    for location_item in location_list:
        placeName = location_item.get('placeName')
        stAddr = location_item.get('stAddr')
        stName = location_item.get('stName')
        zone = location_item.get('zone')

        location_object = Location(placeName,stAddr,stName,zone)

        location_results.append(location_object)

        
        

    
    return location_results




