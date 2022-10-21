import sys
import getopt

def args_help(argv):
    message_template = """
    usage: {0} [-o | --option] [-m | --meeting] [-sd | --startd] [-ed | --endd]

    Common comands:
    -o  | --option   Option to process request [1,2]
    -m  | --meeting  Name of meeting to search for
    -sd | --startd   Start date of meeting (YYYY-MM-DD format)
    -ed | --endd     End date of meeting (YYYY-MM-DD format)

    Example:
    1) main.py -o 1 -m general -sd 2022-09-10 -ed 2022-09-20
    2) main.py --option 1 --meeting general --startd 2022-09-10 --endd 2022-09-20

    """.format(argv[0])
    print(message_template)

def args_processor(argv):
    args_dict = {}

    try:
        opts, args = getopt.getopt(
            argv[1:], 
            "h:o:m:sd:ed:", ["help", "option=", "meeting=", "startd=", "endd="]
        )
    except:
        args_help(argv)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            args_help(argv)
            sys.exit(2)
        elif opt in ("-o", "--option"):
            args_dict['o'] = arg 
        elif opt in ("-m", "--meeting"):
            args_dict['m'] = arg 
        elif opt in ("-sd", "--startd"):
            args_dict['sd'] = arg 
        elif opt in ("-ed", "--endd"):
            args_dict['ed'] = arg 
    
    """ print('o:', arg_option)
    print('m:', arg_meeting_name)
    print('s:', arg_start_date)
    print('e:', arg_end_date) """
    return args_dict

def are_args():
    if 