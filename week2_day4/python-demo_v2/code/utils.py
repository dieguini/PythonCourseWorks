from datetime import datetime

def get_timestamp_string():
    return datetime.now().strftime("%Y%m%d%H%M%S")

def get_filename(prefix="log", extension="txt"):
    """
    Build filename using:
     'prefix' => Strign
     'suffix' => Build from timestamp yyyymmHHMMSS
     'extension' => String 
    Output is: 'prefix'_'sufix'.'extension'
    """
    return "{}_{}.{}".format(prefix, get_timestamp_string(), extension)

def get_date_log_folder():
    return datetime.now().strftime("%Y%m%d")