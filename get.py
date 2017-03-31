import json
from record import Record
import urllib2
import urllib

def get_data():
    
    url = 'https://data.boston.gov/api/action/datastore_search?resource_id=062fc6fa-b5ff-4270-86cf-202225e40858'
    request = urllib2.Request(url)
    
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        return err

def parse_data(first=0, last=0):
    if (get_data().code == 200):
        the_set = []
        response = get_data()
        data = json.loads(response.read())
        if first and last:
            for row in data['result']['records'][int(first):int(last)]:
                parcel_record = Record(row)
                the_set.append(parcel_record)
            return the_set
        else:
            return get_data().code
        # return the_set
        
    else:
        return get_data().code
    
