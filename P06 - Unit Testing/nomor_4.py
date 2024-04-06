import pytest

def hitung_rata_rata(list_angka):
    if not all(isinstance(i, int) for i in list_angka):
        raise TypeError("List harus berisi angka")
    if len(list_angka) == 0:
        return 0
    return sum(list_angka) / len(list_angka)

def test_hitung_rata_rata():
    assert hitung_rata_rata([1, 2, 3, 4, 5]) == 3
    assert hitung_rata_rata([]) == 0
    with pytest.raises(TypeError):
        hitung_rata_rata([1, 2, "tiga", 4, 5])
