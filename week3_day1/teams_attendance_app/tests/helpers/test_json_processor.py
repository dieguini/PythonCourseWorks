from helpers.json_processor import generate_dict, generate_json


def test_generate_json_true():
    string_meeting_title = 'meeting'
    data = [
        {
            "date": "9/12/2022",
            "duration": "0h 0m"
        },
        {
            "date": "9/13/2022",
            "duration": "0h 0m"
        }
    ]

    expected_response = {
        "meeting_title": string_meeting_title,
        "data": data
    }

    response = generate_json(string_meeting_title, data)
    assert response == expected_response, "Expected response are json objects equal?"


def test_generate_dict_true():
    string_date = '9/13/2022'
    key = 'duration'
    key_variable = '0h 0m'
    expected_result = {
        "date": '9/13/2022',
        'duration': '0h 0m'
    }

    result = generate_dict(string_date, key, key_variable)
    assert result == expected_result, "Expected response dictoinary objects equal?"


def test_generate_json_error_meeting_title_name_false():
    string_meeting_title = 'general meeting name'
    data = [
        {
            "date": "9/12/2022",
            "duration": "0h 0m"
        },
        {
            "date": "9/13/2022",
            "duration": "0h 0m"
        }
    ]

    expected_response = {
        "meeting_title": 'another name',
        "data": data
    }

    response = generate_json(string_meeting_title, data)
    assert_msj = "Expected response are json objects different in meeting name?"
    assert response != expected_response, assert_msj


def test_generate_json_error_data_different_data_false():
    string_meeting_title = 'general meeting name'
    data = [
        {
            "date": "9/12/2022",
            "duration": "0h 0m"
        },
    ]

    expected_response = {
        "meeting_title": 'another name',
        "data": data
    }

    response = generate_json(string_meeting_title, data)
    assert response != expected_response, "Expected response are json objects different in data?"


def test_generate_dict_false():
    string_date = '9/13/2022'
    key = 'duration'
    key_variable = '0h 0m'
    not_expected_result = {
        "date": "0/0/0",
        'another': 'value'
    }

    result = generate_dict(string_date, key, key_variable)

    assert result != not_expected_result, "Expected response dictoinary objects not equal?"
