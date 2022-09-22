from helpers.csv_processor import replace_csv


def test_replace_csv_normal_string_true():
    string_csv = 'Hola, prueba de cadena normal'
    assert replace_csv(string_csv) == ['Hola, prueba de cadena normal'], "Expected response ['Hola']"

def test_replace_csv_format_string_true():
    string_csv = 'H\x00o\x00l\x00a\x00\n'
    assert replace_csv(string_csv) == ['Hola'], "Expected response ['Hola']"


def test_replace_csv_normal_false():
    string_csv = 'Hola que hace\n como esta'
    assert replace_csv(string_csv) != ['Hola que hace'], "Expected response different from ['Hola que hace']"

def test_replace_csv_format_false():
    string_csv = 'H\x00o\x00l\x00a\x00que hace\n'
    assert replace_csv(string_csv) != ['Hola'], "Expected response different from ['Hola']"