"""
1. Read CSV files and returns in-memory object
"""
import os
import logging
from token import AT
from datetime import datetime, timedelta
from helpers import json_processor
from helpers import dates_helper

ATTENDANCE_REPORT_FOLDER_NAME = 'attendace_reports'

def is_valid_path(path):
    if os.path.exists(path):
        return True

    return False

def read_line(file_lines, line_number):
    return  file_lines[line_number]

def replace_csv(csv_string):
    return csv_string.replace('\x00','').replace('\n','').split('\t')

def reads_attendance_reports(meeting_name,start_date, end_date, option):
    """
        Option=1 => Number of participants
        Option=2 => Duration of meeting
    """
    
    # Validates 'attendance 'folder exists
    if not is_valid_path(ATTENDANCE_REPORT_FOLDER_NAME):
        warning_message = " Error: 'attendace_reports' folder doesn't exists" 
        logging.warning(warning_message)
        return

    option = "2"
    meeting_name = "general"
    start_date = "2022-9-9"
    end_date = "2022-9-18"

    start_date = dates_helper.string_to_date(start_date)
    end_date = dates_helper.string_to_date(end_date)
    
    list_search_range = dates_helper.list_date_range(start_date, end_date)
    
    # Just list that matches
    data = []

    for search in list_search_range:
        path_sub_folder = os.path.join(ATTENDANCE_REPORT_FOLDER_NAME, search)
        string_date = dates_helper.date_format(search)
        
        if os.path.exists(path_sub_folder):
            # Lists all file .csv inside folder
            for csv_file_name in os.listdir(path_sub_folder):
                #Asks if contains meeting name
                cont_files = 0

                if csv_file_name.lower().__contains__(meeting_name):
                    path_file = os.path.join(path_sub_folder,csv_file_name)
                    # Opens path to read file
                    with open(path_file, 'r') as csv_file:
                        file_lines = csv_file.readlines()
                        # Gets lines of interest
                        number_participants = read_line(file_lines, 1)
                        meeting_start_time = read_line(file_lines, 3)
                        meeting_end_time = read_line(file_lines, 4)
                        
                        if option == "1": # Number participants
                            list_number_participants = replace_csv(number_participants)
                            key = "participants"
                            key_variable = int(list_number_participants[1])
                        elif option == "2": # Duration meeting
                            list_meeting_start_time = replace_csv(meeting_start_time)
                            list_meeting_end_time = replace_csv(meeting_end_time)
                            
                            start_time = dates_helper.string_to_date(list_meeting_start_time[1],format_date='%m/%d/%Y, %H:%M:%S %p')
                            end_time = dates_helper.string_to_date(list_meeting_end_time[1],format_date='%m/%d/%Y, %H:%M:%S %p')
                            
                            key = "duration"
                            key_variable = dates_helper.diff_hour_minute(end_time, start_time)
                    
                    cont_files = len(os.listdir(path_sub_folder))
                    break
                else:
                    if option == "1":
                        key = "participants"
                        key_variable = -99999
                    elif option == "2":
                        key = "duration"
                        key_variable = "0h 0m"
                    cont_files += 1
            
            if cont_files == len(os.listdir(path_sub_folder)):
                dictionary_format = json_processor.generate_dict(string_date, key, key_variable)
                data.append(dictionary_format)
        else:
            if option == "1":
                key = "participants"
                key_variable = -99999
            elif option == "2":
                key = "duration"
                key_variable = "0h 0m"

            dictionary_format = json_processor.generate_dict(string_date, key, key_variable)
            data.append(dictionary_format)
        
    json_data = json_processor.generate_json(meeting_name.title(), data)
    json_processor.print_json(json_data)