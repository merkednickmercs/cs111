from byu_pytest_utils import max_score, this_folder, with_import


@max_score(2.5)
@with_import('lab03', 'even_weighted')
def test_even_weighted_1_2_3_4_5_6(even_weighted):
    assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]


@max_score(2.5)
@with_import('lab03', 'even_weighted')
def test_even_weighted_9_17_4_5_4(even_weighted):
    assert even_weighted([9, 17, 4, 5, 4]) == [0, 8, 16]


@max_score(2.5)
@with_import('lab03', 'couple')
def test_couple_1_2_3_4_5_6(couple):
    assert couple([1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]


@max_score(2.5)
@with_import('lab03', 'couple')
def test_couple_c_6_s_1(couple):
    assert couple(['c', 6], ['s', '1']) == [['c', 's'], [6, '1']]


@max_score(5)
@with_import('lab03', 'count_appearances')
def test_count_appearances(count_appearances):
    assert count_appearances([0]) == {0: 1}
    assert count_appearances([0, 0, 1, 2, 1, 1]) == {0: 2, 1: 3, 2: 1}
    assert count_appearances([0, 0, 0, 0, 0, 3, 0, 0]) == {0: 7, 3: 1}


@max_score(5)
@with_import('lab03', 'copy_file')
def test_copy_file(copy_file):
    KEY = """1: They say you should never eat dirt.
2: It's not nearly as good as an onion.
3: It's not as good as the CS pun on my shirt."""
    copy_file(this_folder / 'text.txt', this_folder / 'output.txt')
    with open(this_folder / 'output.txt', 'r') as fin:
        assert fin.read() == KEY
