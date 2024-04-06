import pytest

def balik_string(s):
    return s[::-1]

def test_balik_string():
    assert balik_string("abcde") == "edcba"
    assert balik_string("ABCDE") == "EDCBA"
    assert balik_string("AbCdE") == "EdCbA"
    assert balik_string("") == ""
