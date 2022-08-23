import pytest

def kth_stat(lst, n):
    return sorted(lst)[n]

@pytest.mark.parametrize(
    ('values', 'stat_order', 'expected'), [
        ([1], 0, 1),
        ([1, 1, 1, 1, 1], 4, 1),
        (range(100), 4, 3)
    ]
)
def test_on_range(values, stat_order, expected):
    assert kth_stat(values, stat_order) == expected