## app entry point

from helpers.data_processor import reads_attendance_reports
from helpers.dates_helper import string_to_date

def is_valid_option(selected_option):
    """
        Function that validates if question is ok
        returns True => valid question
                False => invalid question

        valid options => '1','2' or 'q'
    """
    if selected_option == '1':
        return True
    
    if selected_option == '2':
        return True
    
    if selected_option == 'q':
        return True
    
    return False

def process_questions():
    ## display questions menu
    ## drive "question" selection while not Quit
    """
        returns number
    """
    selected_option = None 
    print('Please select an option')
    print('-----------------------')
    # TODO make markdown questions
    template_question = "1. What is the number of Partipants attending 'meeting_name' Meeting per date, date filter between 'start_date' and 'end_date'\n"
    template_question += "2. What is the duration of 'meeting_name' Meeting per date, date filter between 'start_date' and 'end_date'\n\n"
    template_question += "Q. Quit\n"

    print(template_question)

    selected_option = input('Option: ').lower()
    valid_option = is_valid_option(selected_option)

    while not valid_option:
        print('Invalid option! Pick again')
        selected_option = input('Option: ').lower()
        valid_option = is_valid_option(selected_option)

    return selected_option

def process_question_options():
    ## display input to request meeting name, end and start date
    ## drive "input" aquisition while not Quit
    
    meeting_name = input('Enter meeting name: ')
    # TODO make mask input on date
    start_date_input = input('Enter a start date in YYYY-MM-DD format: ')

    # TODO Validates dates before reading attendance report
    end_date_input = input('Enter a end date in YYYY-MM-DD format: ')

    #start_date = string_to_date(start_date, format_date='%Y-%m-%d')

    arguments = {
        'meeting_name': meeting_name,
        'start_date': start_date_input,
        'end_date': end_date_input
    }
    return arguments

def welcome():
    print('########################################')
    print('##         TEAM ATTENDANCE APP        ##')
    print('########################################\n')

def main():
    welcome()

    option  = process_questions()
    print('Option selected: ',option)

    arguments =  process_question_options()

    reads_attendance_reports(
        arguments.get('meeting_name'), 
        arguments.get('start_date'), 
        arguments.get('end_date'),
        option
    )

main()