from byu_pytest_utils import max_score, with_import


@max_score(2.5)
@with_import('lab02', 'falling')
def test_falling_6_3(falling):
    assert falling(6, 3) == 120


@max_score(2.5)
@with_import('lab02', 'falling')
def test_falling_4_3(falling):
    assert falling(4, 3) == 24


@max_score(2.5)
@with_import('lab02', 'falling')
def test_falling_4_1(falling):
    assert falling(4, 1) == 4


@max_score(2.5)
@with_import('lab02', 'falling')
def test_falling_4_0(falling):
    assert falling(4, 0) == 1


@max_score(2.5)
@with_import('lab02', 'sum_digits')
def test_sum_digits_10(sum_digits):
    assert sum_digits(10) == 1


@max_score(2.5)
@with_import('lab02', 'sum_digits')
def test_sum_digits_4224(sum_digits):
    assert sum_digits(4224) == 12


@max_score(2.5)
@with_import('lab02', 'sum_digits')
def test_sum_digits_1234567890(sum_digits):
    assert sum_digits(1234567890) == 45


@max_score(2.5)
@with_import('lab02', 'sum_digits')
def test_sum_digits_123(sum_digits):
    assert sum_digits(123) == 6
