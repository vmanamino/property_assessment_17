import json
from record import Record
import urllib2
import urllib

def get_data(offset):
    
    url = 'https://data.boston.gov/api/action/datastore_search?offset='+str(offset)+'&resource_id=062fc6fa-b5ff-4270-86cf-202225e40858'
    request = urllib2.Request(url)
    
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        return err

def parse_data(offset):
    the_set = []
    response = get_data(offset)
    data = json.loads(response.read())
    
    for row in data['result']['records']:
        parcel_record = Record(row)
        the_set.append(parcel_record)
        
    return the_set

def total(offset):
    response = get_data(offset)
    data = json.loads(response.read())
    total = data['result']['total']
    return total
    
    
