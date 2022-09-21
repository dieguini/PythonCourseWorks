"""
1. Genenerates JSON from in-memory object
2. Writes in-memory object into JSON file
"""
import json

def generate_json(string_meeting_title, list_data):
    json = {   
        "meeting_title": string_meeting_title,
        "data": list_data
    }
    return json

def generate_dict(string_date, key, key_variable):
    
    dictionary = {
        "date": string_date,
        key: key_variable
    }
    return dictionary

def print_json(json_string):
    print(json.dumps(json_string, indent=4))

def writes_json_file():
    pass