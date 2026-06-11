import pytest

from pyar.core import add_two_numbers


@pytest.mark.parametrize(
    "a, b, expected, boundary_type",
    [
        (0, 0, 0, "Sum of zero and zero is zero"),
        (-1, 1, 0, "Positive and negative of same magnitude sums to zero"),
        (500_000, 500_000, 1_000_000, "Sum of two positive numbers is correct."),
    ],
)
def test_add_two_numbers_boundaries(a, b, expected, boundary_type):
    """
    Illustration of how you might parameterize a pytest function with several
    meaningful boundary values.

    We'll delete this at some point, it's primarily meant to show the concept
    on a toy example.
    """
    result = add_two_numbers(a, b)
    assert (
        result == expected
    ), f"Failed on {boundary_type}: result {result} != expected {expected}"
