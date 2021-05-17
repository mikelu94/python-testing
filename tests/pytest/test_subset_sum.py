from src import subset_sum


def test_exists_subset_sum():
    assert subset_sum([1, 2, 3, 4, 5], 15) is True


def test_not_exists_subset_sum():
    assert subset_sum([1, 2, 3, 4, 5], 16) is False


def test_zero_subset_sum():
    assert subset_sum([], 0) is True
