from src.helpers.files_helper import is_valid_path, build_full_filename


def is_valid_path_none_returns_false():
    result = is_valid_path(None)
    print(not result)
    assert not result, 'expected False for path=None'
    assert not result, 'expected False for path=None'


def is_valid_path_empty_returns_true():
    result = is_valid_path('')
    print(not result)
    assert result, "expected True for path=''"
    assert result, "expected True for path=''"


def is_valid_path_non_empty_path_returns_true():
    path = "output"
    result = is_valid_path(path)
    assert result, "expected True for path={path}"
    assert result, "expected True for path={path}"


def build_full_filename_empty_path():
    path = ""
    filename = "x.txt"
    full_filename = build_full_filename(path, filename)

    # expected `x.txt`
    message = 'expected full_filename = {filename}'
    assert full_filename is not None and not ('/' in full_filename), message


# def main():
#     is_valid_path_none_returns_false()
#     is_valid_path_empty_returns_true()
#     is_valid_path_non_empty_path_returns_true()
#     build_full_filename_empty_path()

# main()
