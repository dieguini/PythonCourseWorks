from helpers.data_processor import is_valid_path, returns_json_attendance_reports


def test_is_valid_path_att_rep_true():
    att_rep_fold_name = 'attendace_reports'
    assert is_valid_path(att_rep_fold_name), 'Exists path of folder exists'

def test_is_valid_path_att_rep_false():
    another_fold_name = 'another_ridiculouse_folder_name'
    assert not is_valid_path(another_fold_name), "Exists path of folder doesn't exists"

def test_returns_json_attendance_reports_general_numerber_participants_true():
    meeting_name='general'
    start_date='2022-9-10'
    end_date='2022-9-17'
    option='1' # Participants

    expected_result = {
        "meeting_title": "General",
        "data": [
            {
                "date": "9/10/2022",
                "participants": -99999
            },
            {
                "date": "9/11/2022",
                "participants": -99999
            },
            {
                "date": "9/12/2022",
                "participants": -99999
            },
            {
                "date": "9/13/2022",
                "participants": -99999
            },
            {
                "date": "9/14/2022",
                "participants": -99999
            },
            {
                "date": "9/15/2022",
                "participants": -99999
            },
            {
                "date": "9/16/2022",
                "participants": 22
            },
            {
                "date": "9/17/2022",
                "participants": -99999
            }
        ]
    }

    result = returns_json_attendance_reports(
        meeting_name,
        start_date, 
        end_date, 
        option
        )
    assert expected_result == result, "Json reports are not equal"

def test_returns_json_attendance_reports_general_numerber_participants_false():
    meeting_name='asd'
    start_date='2022-9-10'
    end_date='2022-9-17'
    option='1' # Participants

    not_expected_result = {
        "meeting_title": "General",
        "data": [
            {
                "date": "9/10/2022",
                "participants": -99999
            },
            {
                "date": "9/11/2022",
                "participants": -99999
            }
        ]
    }

    result = returns_json_attendance_reports(
        meeting_name,
        start_date, 
        end_date, 
        option
        )
    assert not_expected_result != result, "Json reports are equal"