import pytest

def urutkan_list(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return list

def test_urutkan_list():
    assert urutkan_list([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
    assert urutkan_list(["d", "a", "c", "b"]) == ["a", "b", "c", "d"]
    assert urutkan_list([]) == []
    with pytest.raises(TypeError):
        urutkan_list([1, "dua", 3, "empat"])

