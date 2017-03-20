import json
import urllib2
import urllib

def get_data():
    
    url = 'https://data.boston.gov/api/action/datastore_search?resource_id=9a4b1173-89ac-4a01-93e7-661eeb81ba16'
    request = urllib2.Request(url)
    
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        return err

def parse_data():
    if (get_data().code == 200):
        response = get_data()
        data = json.loads(response.read())
        print(len(data['result']['records']))
        
    else:
        print(get_data().code)
    