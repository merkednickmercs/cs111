from byu_pytest_utils import max_score, with_import


@max_score(2.5)
@with_import('sand_functional', 'is_move_ok')
@with_import('Grid', 'Grid')
def test_is_move_ok_out_of_bounds(Grid, is_move_ok):
    grid = Grid.build([['s']])
    assert not is_move_ok(grid, 0, 0, -1, 1)
    assert not is_move_ok(grid, 0, 0, 0, 1)
    assert not is_move_ok(grid, 0, 0, 1, 1)


@max_score(2.5)
@with_import('sand_functional', 'is_move_ok')
@with_import('Grid', 'Grid')
def test_is_move_ok_cant_move(Grid, is_move_ok):
    grid = Grid.build([[None, 's', None], ['r', 's', 's']])
    assert not is_move_ok(grid, 1, 0, 0, 1)
    assert not is_move_ok(grid, 1, 0, 1, 1)
    assert not is_move_ok(grid, 1, 0, 2, 1)


@max_score(2.5)
@with_import('sand_functional', 'is_move_ok')
@with_import('Grid', 'Grid')
def test_is_move_ok_straight_down(Grid, is_move_ok):
    grid = Grid.build([['s'], [None]])
    assert is_move_ok(grid, 0, 0, 0, 1)


@max_score(2.5)
@with_import('sand_functional', 'is_move_ok')
@with_import('Grid', 'Grid')
def test_is_move_ok_down_left(Grid, is_move_ok):
    grid = Grid.build([[None, 's'], [None, 'r']])
    assert is_move_ok(grid, 1, 0, 0, 1)


@max_score(2.5)
@with_import('sand_functional', 'is_move_ok')
@with_import('Grid', 'Grid')
def test_is_move_ok_down_right(Grid, is_move_ok):
    grid = Grid.build([[None, 's', None], ['r', 's', None]])
    assert is_move_ok(grid, 1, 0, 2, 1)


@max_score(2.5)
@with_import('sand_functional', 'is_move_ok')
@with_import('Grid', 'Grid')
def test_is_move_ok_corner_rule(Grid, is_move_ok):
    grid = Grid.build([['r', 's', 'r'], [None, 's', None]])
    assert not is_move_ok(grid, 1, 0, 0, 1)
    assert not is_move_ok(grid, 1, 0, 2, 1)


@max_score(2.5)
@with_import('sand_functional', 'do_move')
@with_import('Grid', 'Grid')
def test_do_move_1(Grid, do_move):
    key = Grid.build([[None, None, None], [None, 's', None]])
    input = Grid.build([[None, 's', None], [None, None, None]])
    output = do_move(input, 1, 0, 1, 1)
    assert output == key


@max_score(2.5)
@with_import('sand_functional', 'do_move')
@with_import('Grid', 'Grid')
def test_do_move_2(Grid, do_move):
    key = Grid.build([[None, None], ['s', 'r']])
    input = Grid.build([[None, 's'], [None, 'r']])
    output = do_move(input, 1, 0, 0, 1)
    assert output == key


@max_score(2.5)
@with_import('sand_functional', 'do_gravity')
@with_import('Grid', 'Grid')
def test_do_gravity_out_of_bounds(Grid, do_gravity):
    key = Grid.build([['s']])
    input = Grid.build([['s']])
    output = do_gravity(input, 0, 0)
    assert output == key


@max_score(2.5)
@with_import('sand_functional', 'do_gravity')
@with_import('Grid', 'Grid')
def test_do_gravity_cant_move(Grid, do_gravity):
    key = Grid.build([[None, 's', None], ['s', 's', 's']])
    input = Grid.build([[None, 's', None], ['s', 's', 's']])
    output = do_gravity(input, 1, 0)
    assert output == key


@max_score(2.5)
@with_import('sand_functional', 'do_gravity')
@with_import('Grid', 'Grid')
def test_do_gravity_straight_down(Grid, do_gravity):
    key = Grid.build([[None], ['s']])
    input = Grid.build([['s'], [None]])
    output = do_gravity(input, 0, 0)
    assert output == key


@max_score(2.5)
@with_import('sand_functional', 'do_gravity')
@with_import('Grid', 'Grid')
def test_do_gravity_down_left(Grid, do_gravity):
    key = Grid.build([[None, None], ['s', 'r']])
    input = Grid.build([[None, 's'], [None, 'r']])
    output = do_gravity(input, 1, 0)
    assert output == key


@max_score(2.5)
@with_import('sand_functional', 'do_gravity')
@with_import('Grid', 'Grid')
def test_do_gravity_down_right(Grid, do_gravity):
    key = Grid.build([['r', None, None], ['r', 's', 's']])
    input = Grid.build([['r', 's', None], ['r', 's', None]])
    output = do_gravity(input, 1, 0)
    assert output == key


@max_score(2.5)
@with_import('sand_functional', 'do_gravity')
@with_import('Grid', 'Grid')
def test_do_gravity_corner_rule(Grid, do_gravity):
    key = Grid.build([['r', 's', 'r'], [None, 'r', None]])
    input = Grid.build([['r', 's', 'r'], [None, 'r', None]])
    output = do_gravity(input, 1, 0)
    assert output == key


@max_score(5)
@with_import('sand_functional', 'do_whole_grid')
@with_import('Grid', 'Grid')
def test_do_whole_grid_all_falling_rules(Grid, do_whole_grid):
    key = Grid.build(
        [[None, 's', None, None, None, None, None, None],
         ['r', 's', 'r', 's', 'r', 's', 'r', 's'],
         [None, 'r', None, None, None, 'r', None, None]]
    )
    input = Grid.build(
        [[None, 's', None, None, 's', 's', 's', None], 
         ['r', 's', 'r', None, 'r', None, 'r', None],
         [None, 'r', None, None, None, 'r', None, None]]
    )
    output = do_whole_grid(input)
    assert output == key


@max_score(5)
@with_import('sand_functional', 'do_whole_grid')
@with_import('Grid', 'Grid')
def test_do_whole_grid_sand_falls_together(Grid, do_whole_grid):
    key = Grid.build([[None], ['s'], ['s'], ['s'], ['s']])
    input = Grid.build([['s'], ['s'], ['s'], ['s'], [None]])
    output = do_whole_grid(input)
    assert output == key


@max_score(5)
@with_import('sand_functional', 'do_whole_grid')
@with_import('Grid', 'Grid')
def test_do_whole_grid_until_sand_settles(Grid, do_whole_grid):
    keys = [
        Grid.build(
            [[None, None, None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             ['s', 's', None]]
        ),
        Grid.build(
            [[None, None, None],
             [None, None, None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             ['s', 's', 's']]
        ),
        Grid.build(
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, 's', None],
             ['s', 's', None],
             ['s', 's', 's']]
        ),
        Grid.build(
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, None, None],
             ['s', 's', 's'],
             ['s', 's', 's']]
        ),
        Grid.build(
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, None, None],
             ['s', 's', 's'],
             ['s', 's', 's']]
        )
    ]
    input = Grid.build(
        [[None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None]]
    )
    output = input
    for key in keys:
        output = do_whole_grid(output)
        assert output == key
