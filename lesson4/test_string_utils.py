import pytest
from string_utils import StringUtils

stringutils = StringUtils()


@pytest.mark.parametrize("string, result", [
    ("", ""),
    (" ", " "),
    ("test", "Test"),
    ("123456", "123456"),
    ("длинное предложение из нескольких слов", "Длинное предложение из нескольких слов")
])
def test_capitalize(string, result):
    res = stringutils.capitilize(string)
    assert res == result


@pytest.mark.parametrize("string, result", [
    ("", ""),
    (" test", "test"),
    ("  test", "test")
])
def test_trim(string, result):
    res = stringutils.trim(string)
    assert res == result


@pytest.mark.parametrize("string, delimeter, result", [
    ("", ":", []),
    (" ", ":", []),
    ("a,b,c", ",", ["a", "b", "c"]),
    ("1:2:3", ":", ["1", "2", "3"])
])
def test_to_list(string, delimeter, result):
    assert stringutils.to_list(string, delimeter) == result


@pytest.mark.parametrize("string, symbol, result", [
    ("Test", "T", True),
    ("Test", "R", False),
    ("", "E", False),
    ("  ", "N", False)
])
def test_contains(string, symbol, result):
    res = stringutils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("", "A", ""),
    ("  ", "  ", ""),
    ("Test", "s", "Tet"),
    ("Tests", "s", "Tet")

])
def test_delete_symbol(string, symbol, result):
    res = stringutils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("", "t", False),
    ("  ", "t", False),
    ("Test", "T", True),
    ("Test", "e", False)
])
def test_starts_with(string, symbol, result):
    res = stringutils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("Test", "t", True),
    ("Test", "s", False),
    ("", "t", False),
    ("  ", "t", False)
])
def test_end_with(string, symbol, result):
    res = stringutils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("Test", False),
    ("t", False),
    ("123", False),
])
def test_is_empty(string, result):
    res = stringutils.is_empty(string)
    assert res == result


@pytest.mark.parametrize("lst, joiner, expected", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Test1", "Test2"], ", ", "Test1, Test2"),
    (["Test", "SkyPro"], "-", "Test-SkyPro"),
    ([], "- ", "" )
])
def test_list_to_string(lst, joiner, expected):
    res = stringutils.list_to_string(lst, joiner)
    assert res == expected