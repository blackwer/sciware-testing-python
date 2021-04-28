import pytest
import sciware_testing_python


def test_sum1():
    # basic sanity test: do we get the right answer for a simple case?
    assert sciware_testing_python.sum_numbers([1, 2, 3]) == 6


def test_sum2():
    # what's the sum of an empty list
    assert sciware_testing_python.sum_numbers([]) == 0


def test_sum_bools():
    try:
        sciware_testing_python.sum_numbers([False, True])
    except ValueError:
        return True
    return False


def test_add_vectors():
    assert sciware_testing_python.add_vectors([1, 2], [2, 3]) == [3, 5]
