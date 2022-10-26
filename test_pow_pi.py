import pytest
from defs_for_test import pow_pi


@pytest.mark.parametrize('a, expected_result', [
    (0.01, 3.14),
    (0.02, 3.14),
    (0.001, 3.141),
    (0.000005, 3.14159),
    (1, 3.0)])
def test_pow_pi(a, expected_result):
    assert pow_pi(a) == expected_result
