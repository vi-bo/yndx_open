import math
from unittest.mock import patch

def test_patch_sin():
    with patch('math.sin', return_value=2) as m:
        assert math.sin(0) == 2
        assert math.sin(1) == 2
        assert m.call_count == 2