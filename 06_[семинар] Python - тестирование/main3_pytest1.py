import pytest
import sys
import json


def test_raises():
    with pytest.raises(IndexError):
        kth_stat(1, 0)

@pytest.mark.xfail()
def test_raises():
    kth_stat([1, 2, 3], 100)

@pytest.mark.skipif(
    sys.platform == 'linux',
    reason='don\'t know why, but may fail on linux')
def test_not_to_run_on_linux(filled_file):
    assert kth_stat(json.load(filled_file), 500) == 499