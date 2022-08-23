from hypothesis import given
from hypothesis.strategies import lists, integers

def broken_sort(it):
    if len(it) == 5:
        return it
    return sorted(it)

@given(lists(integers()))
def test_sort(it):
    assert broken_sort(it) == sorted(it)