import pytest

def luas_persegi_panjang(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Parameter harus berupa angka")
    return a * b

def test_luas_persegi_panjang():
    assert luas_persegi_panjang(5, 2) == 10
    assert luas_persegi_panjang(0, 0) == 0
    with pytest.raises(TypeError):
        luas_persegi_panjang("lima", 2)
    with pytest.raises(TypeError):
        luas_persegi_panjang(2, "dua")
