import pytest
from defs_for_test import pow_pi


@pytest.mark.parametrize('expected_exception, a', [
    (ZeroDivisionError, 0),
    (ZeroDivisionError, '0'),
    (ValueError, 'm')])
def test_errors(expected_exception, a):
    with pytest.raises(expected_exception):
        pow_pi(a)