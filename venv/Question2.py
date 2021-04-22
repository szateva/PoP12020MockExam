import pytest

def test_delete_all1():
    s = "helloworldhiworldyes"
    what = "world"
    assert delete_all(s, what) == "hellohiyes"

def test_delete_all2():
    s = ""
    what = "hi"
    assert delete_all(s, what) == ""

def test_delete_all3():
    s = "hellobellamy"
    what = "ola"
    assert delete_all(s, what) == "hellobellamy"

def test_delete_all4():
    s = 5674582
    what = 5
    with pytest.raises(Exception):
        assert delete_all(s, what)

def test_delete_all5():
    s = "hellosevenfive"
    what = 5
    with pytest.raises(Exception):
        assert delete_all(s, what)