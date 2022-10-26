import pytest
from defs_for_test import prime_factors


@pytest.mark.parametrize('a, expected_result', [
    (0, []),
    (1, []),
    (2, [2]),
    (15, [3, 5]),
    (25, [5, 5])])
def test_prime_factors(a, expected_result):
    assert prime_factors(a) == expected_result
