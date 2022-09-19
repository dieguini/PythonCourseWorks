from sqlite3 import NotSupportedError
import requests
import logging

## Json URL
URL = 'https://pythoncourseweek2day4-2.free.beeceptor.com/my/api/path?Content-Type=application/json'
## Text URL
#URL = 'https://pythoncourseweek2day4-2.free.beeceptor.com/my/api/path'

def get_demo_api_data():
    """
    GET data from Rest Api endpoint
        Depends on 'Content-Type' => json, text
    """
    response = requests.get(URL)
    if response.status_code != 200:
        logging.error(f'API returned {response.status_code}')
        #raise Exception(f'API returned {response.status_code}')

    response_data = ""
    extension = ""
    if response.headers.get('Content-Type') == 'text/plain':
        response_data = response.text
        extension = "txt"
    elif response.headers.get('Content-Type') == 'application/json':
        response_data = response.json()
        extension = "json"
    else:
        raise NotSupportedError

    return response.status_code, response_data, extension