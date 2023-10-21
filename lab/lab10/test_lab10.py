from byu_pytest_utils import max_score, with_import
import random


def build_grid(Grid, lst):
    assert isinstance(lst, list)
    height = len(lst)
    assert height != 0
    for row in lst:
        assert isinstance(row, list)
    width = len(lst[0])
    for row in lst[1:]:
        assert len(row) == width

    grid = Grid(width, height)
    for y, row in zip(range(height), lst):
        for x, space in zip(range(width), row):
            grid.set(x, y, space)
    return grid


@max_score(4)
@with_import('lab10', 'random_rocks')
@with_import('Grid', 'Grid')
def test_random_rocks(Grid, random_rocks):
    input = build_grid(
        Grid,
        [[None, 't', None, None],
         [None, None, None, None],
         [None, None, None, None]]
    )
    key = build_grid(
        Grid,
        [[None, 't', 'r', 'r'],
         [None, 'r', 'r', None],
         ['r', None, 'r', None]]
    )

    random.seed(22)
    output = random_rocks(input, 0.4)
    assert output == key
    assert input != output, 'random_rocks must return a (modified) copy of the original Grid'


@max_score(4)
@with_import('lab10', 'random_bubbles')
@with_import('Grid', 'Grid')
def test_random_bubbles(Grid, random_bubbles):
    input = build_grid(
        Grid,
        [[None, None, None],
         [None, None, 't'],
         [None, None, None],
         [None, None, None]]
    )
    key = build_grid(
        Grid,
        [[None, None, None],
         ['b', None, 't'],
         [None, None, 'b'],
         [None, 'b', 'b']]
    )

    random.seed(10)
    output = random_bubbles(input, 0.35)
    assert output == key
    assert input != output, 'random_bubbles must return a (modified) copy of the original Grid'


@max_score(4)
@with_import('lab10', 'modify_grid')
@with_import('Grid', 'Grid')
def test_modify_grid(Grid, modify_grid):
    grid = build_grid(
        Grid,
        [[None, None, None, None, None, None],
         ['t', None, None, None, None, None]]
    )
    key = build_grid(
        Grid,
        [['s', None, None, 's', 's', None],
         ['t', None, 's', 's', 's', 's']]
    )

    random.seed(21)
    modify_grid(grid, lambda x, y: grid.set(x, y, 's'), 0.53)
    assert grid == key


@max_score(2)
@with_import('lab10', 'bubble_up')
@with_import('Grid', 'Grid')
def test_bubble_up(Grid, bubble_up):
    input = build_grid(
        Grid,
        [[None],
         ['b']]
    )
    key = build_grid(
        Grid,
        [['b'],
         [None]]
    )
    output = bubble_up(input, 0, 1)
    assert output == key
    assert input != output, 'bubble_up must return a (modified) copy of the original Grid'


@max_score(6)
@with_import('lab10', 'move_bubbles')
@with_import('Grid', 'Grid')
def test_move_bubbles(Grid, move_bubbles):
    input = build_grid(
        Grid,
        [['b', None, None],
         ['b', 'b', 'b'],
         [None, 'b', None]]
    )
    key = build_grid(
        Grid,
        [['b', 'b', 'b'],
         ['b', 'b', None],
         [None, None, None]]
    )

    output = move_bubbles(input)
    assert output == key
    assert input != output, 'move_bubbles must return a (modified) copy of the original Grid'
