from exex_cli import convert


def test_to_string():
    assert convert.to_string(None) == ""
    assert convert.to_string("None") == "None"
    assert convert.to_string(1) == "1"
    assert convert.to_string("a") == "a"
    assert convert.to_string(False) == ""
    assert convert.to_string("False") == "False"
    assert convert.to_string([]) == ""


def test_to_strings():
    assert convert.to_strings(None) == ""
    assert convert.to_strings("None") == "None"
    assert convert.to_strings(1) == "1"
    assert convert.to_strings("a") == "a"
    assert convert.to_strings(False) == ""
    assert convert.to_strings("False") == "False"
    assert convert.to_strings([]) == ""
    assert convert.to_strings(["a"]) == ["a"]
    assert convert.to_strings([1]) == ["1"]
    assert convert.to_strings([["a", 1], ["b", 2]]) == [["a", "1"], ["b", "2"]]


def test_to_csv():
    assert convert.to_csv(None) == ""
    assert convert.to_csv("None") == "None"
    assert convert.to_csv(1) == "1"
    assert convert.to_csv("a") == "a"
    assert convert.to_csv(False) == ""
    assert convert.to_csv("False") == "False"
    assert convert.to_csv([]) == ""
    assert convert.to_csv(["a"]) == "a"
    assert convert.to_csv(["a", "b", 3]) == "a\nb\n3"
    assert convert.to_csv([1]) == "1"
    assert convert.to_csv([["a", 1], ["b", 2]]) == "a,1\nb,2"
