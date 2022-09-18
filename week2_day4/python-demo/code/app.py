"""
    Entry point for my application
"""
import utils
from rest_client import get_demo_api_data

from files_helper import write_data_in_file
from files_helper import create_output_folder

def main():
    print("Copying contents APP - API Rest")
    status_code, response_data, extension = get_demo_api_data()

    if status_code != 200:
        print("Can't continue, API not working")
        return

    file_name = utils.get_filename(extension=extension)

    create_output_folder()
    write_data_in_file(response_data, file_name)

    
main()