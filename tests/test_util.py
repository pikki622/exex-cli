from exex_cli.util import array_dimensions


def test_util():
    assert array_dimensions(None) == (0, 0)
    assert array_dimensions(1) == (0, 0)
    assert array_dimensions("a") == (0, 0)
    assert array_dimensions(False) == (0, 0)
    assert array_dimensions([]) == (0, 0)
    assert array_dimensions(["a"]) == (1, 0)
    assert array_dimensions(["a", "b"]) == (2, 0)
    assert array_dimensions([["a"], ["b"]]) == (2, 1)
    assert array_dimensions([["a", "b"], ["b"]]) == (2, 2)
