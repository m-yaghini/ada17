import json
import requests
import os

RESOURCE_URL = "http://srgssr-prod.apigee.net/rts-archives-public-api/archives"
API_KEY = "pbv1Ac9Hgh3OHHho1jUJwGtJwOcfbiLI"
BASE_PATH = '../dataset/'

def build_dict(query = '', minPublicationDate = '', maxPublicationDate = '',minDurationSec = '',
               maxDurationSec = '', mediaTypes = '', enumeratedFacets = '', publicationDateIntervalFacets = '',
               durationSecIntervalFacets = '', start = '', rows=''):
    dict_ = {'apikey' : API_KEY,
             'query' : query,
             'minPublicationDate' : minPublicationDate,
             'maxPublicationDate' : maxPublicationDate,
             'minDurationSec' : minDurationSec,
             'maxDurationSec' : maxDurationSec,
             'mediaTypes' : mediaTypes,
             'enumeratedFacets' : enumeratedFacets,
             'publicationDateIntervalFacets': publicationDateIntervalFacets,
             'durationSecIntervalFacets' : durationSecIntervalFacets,
             'start' : start,
             'rows' : rows}

    return {k: v for k,v in dict_.items() if v}

def request_data_and_write(payload, path=''):
    r = requests.get(RESOURCE_URL, params=payload)
    
    data = r.json()
    number_documents = data['response']['numFound']
    if number_documents <= 0:
        return
    number_rows = 100
    
    if 'rows' in payload and payload['rows'] > 0:
        number_rows = payload['rows']
        
    number_requests = (number_documents + number_rows // 2) // number_rows
    
    if not os.path.exists(BASE_PATH + path):
        os.makedirs(BASE_PATH + path)

    with open(BASE_PATH + path + 'data_0.json', 'w') as outfile:
        json.dump(data, outfile)
        
    for n in range(1,number_requests):
        
        #print(str(n) + '/' + str(number_requests))
        
        next_payload = payload
        next_payload = payload['start'] = n * number_rows
        
        r = requests.get(RESOURCE_URL, params=payload)
        data = r.json()
        
        with open(BASE_PATH + path + 'data_{}.json'.format(n), 'w') as outfile:
            json.dump(data, outfile)
        
def request_data_total():
    payload = build_dict()
    request_data_and_write(payload, 'total/')

def request_data_per_year(year):
    print('requesting for year ' + str(year))
    payload = build_dict(minPublicationDate='{}'.format(year), maxPublicationDate='{}'.format(year))
    request_data_and_write(payload, 'per_year/{}/'.format(year))