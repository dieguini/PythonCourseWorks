import os
import json
import utils
import logging

from pathlib import Path

# Directory
OUTPUT_DIR = "outer"

def is_valid_path(path):
    ## Not defined
    if path is None:
        return False

    if path == '':
        return True

    return True

def create_folder(path):
    # Check folder structure
    if not os.path.exists(path):
        os.mkdir(path)

def create_output_folder():
    create_folder(OUTPUT_DIR)

def get_extension_of_filename(file_name):
    return os.path.splitext(file_name)[1]

def write_data_in_file(data, file_name, target_path=""):
    """
        Write data in 'filename'.
        'filename' lives in 'target_path'
    """

    if not is_valid_path(target_path):
        create_folder(target_path)
    
    # Preguntar si existe el folder deseado
    folder_log_name = utils.get_date_log_folder()

    folder_path = os.path.join(OUTPUT_DIR, folder_log_name)
    create_folder(folder_path)
    
    file_path = os.path.join(target_path, folder_path, file_name)

    file_extension = get_extension_of_filename(file_name)

    with open(file_path, 'w') as openfile:
        if file_extension == '.txt':
            openfile.write(data)
        elif file_extension == '.json':
            json_object = json.dumps(data, indent=4)
            openfile.write(json_object)
        else:
            pass
    print("Contents copied succesfully!")