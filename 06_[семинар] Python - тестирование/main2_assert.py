def _sort(lst):
    return sorted(lst)

def _broken_sort(lst):
    return sorted(lst[1:])

def test_sort():
    lst = [1, 7, 2, 9, 3, 8, 4]
    assert _sort(lst) == [1, 2, 3, 4, 7, 8, 9], "_sort fails"
    assert _broken_sort(lst) == [1, 2, 3, 4, 7, 8, 9], "_broken_sort fails"

if __name__ == '__main__':
    test_sort()