import pytest

def cek_anggota_list(list_angka, elemen):
    return elemen in list_angka

def test_cek_anggota_list():
    assert cek_anggota_list([1, 2, 3, 4, 5], 3) == True
    assert cek_anggota_list([1, 2, 3, 4, 5], 6) == False
    assert cek_anggota_list([], 1) == False
    assert cek_anggota_list([1, 2, 3, 4, 5], "1") == False
