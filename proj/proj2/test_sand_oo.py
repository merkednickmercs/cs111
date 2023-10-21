from byu_pytest_utils import max_score, with_import
from functools import cache


@cache
def make_sand_wrapper_class(Sand):
    class SandWrapper(Sand):
        def __init__(self, grid, x=0, y=0):
            super().__init__(grid, x, y)

        def __str__(self):
            return super().__str__()

        def __repr__(self):
            return str(self)

        def __eq__(self, other):
            if isinstance(other, (Sand, SandWrapper)):
                return str(self) == str(other)
            else:
                return False

        def __hash__(self):
            return hash(str(self))

    return SandWrapper


def build_sandy_grid(Grid, Sand, lst):
    SandWrapper = make_sand_wrapper_class(Sand)

    grid = Grid.build(lst)
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) == 's':
                grid.set(x, y, SandWrapper(grid, x, y))
    return grid


def construct_all_sand_list(Sand, grid):
    all_sand = []
    for y in range(grid.height):
        for x in range(grid.width):
            space = grid.get(x, y)
            if isinstance(space, Sand):
                all_sand.append(space)
    return all_sand


@max_score(2)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_str(Grid, Sand):
    grid = Grid(6, 6)
    assert str(Sand(grid, 1, 2)) == 'Sand(1,2)'
    assert str(Sand(grid, 5, 3)) == 'Sand(5,3)'


@max_score(1.5)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_out_of_bounds(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['s']])
    assert grid.get(0, 0).gravity() is None


@max_score(1.5)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_cant_move(Grid, Sand):
    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', 's', 's']]
    )
    assert grid.get(1, 0).gravity() is None


@max_score(1.5)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_straight_down(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['s'], [None]])
    assert grid.get(0, 0).gravity() == (0, 1)


@max_score(1.5)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_down_left(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [[None, 's'], [None, 'r']])
    assert grid.get(1, 0).gravity() == (0, 1)


@max_score(1.5)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_down_right(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['r', 's', None], ['r', 's', None]])
    assert grid.get(1, 0).gravity() == (2, 1)


@max_score(1.5)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_corner_rule(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['r', 's', 'r'], [None, 'r', None]])
    assert grid.get(1, 0).gravity() is None


@max_score(1)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_out_of_bounds(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [['s']])
    grid = build_sandy_grid(Grid, Sand, [['s']])
    sand = grid.get(0, 0)
    sand.move(sand.gravity)
    assert grid == key


@max_score(1)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_cant_move(Grid, Sand):
    key = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', 's', 's']]
    )
    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', 's', 's']]
    )
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key


@max_score(1)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_straight_down(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [[None], ['s']])
    grid = build_sandy_grid(Grid, Sand, [['s'], [None]])
    sand = grid.get(0, 0)
    sand.move(sand.gravity)
    assert grid == key


@max_score(1)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_down_left(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [[None, None], ['s', 'r']])
    grid = build_sandy_grid(Grid, Sand, [[None, 's'], [None, 'r']])
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key


@max_score(1)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_down_right(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [['r', None, None], ['r', 's', 's']])
    grid = build_sandy_grid(Grid, Sand, [['r', 's', None], ['r', 's', None]])
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key


@max_score(1)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_corner_rule(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [['r', 's', 'r'], [None, 'r', None]])
    grid = build_sandy_grid(Grid, Sand, [['r', 's', 'r'], [None, 'r', None]])
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key


@max_score(3)
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_falling_example(Grid, Sand):
    keys = [
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, 's', None],
             [None, 's', None],
             ['s', 's', None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, 's', None],
             ['s', 's', 's']]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, 's', None],
             ['s', 's', 's']]
        )
    ]
    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, None, None]]
    )
    for key in keys:
        for y in reversed(range(grid.height)):
            for x in range(grid.width):
                elem = grid.get(x, y)
                if isinstance(elem, Sand):
                    elem.move(elem.gravity)
        assert grid == key


@max_score(7.5)
@with_import('sand_oo', 'all_sand')
@with_import('sand_oo', 'add_sand')
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_add_sand(Grid, Sand, add_sand, all_sand, monkeypatch):
    monkeypatch.setattr(Sand, '__repr__', lambda self: str(self))
    monkeypatch.setattr(Sand, '__hash__', lambda self: hash(str(self)))

    key_grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', 's', None],
         [None, 'r', 's']]
    )
    key_all_sand = set(construct_all_sand_list(Sand, key_grid))

    grid = Grid.build(
        [[None, None, None], [None, None, None], [None, 'r', None]])
    add_sand(grid, 1, 0)
    add_sand(grid, 0, 1)
    add_sand(grid, 1, 1)
    add_sand(grid, 2, 2)

    assert grid == key_grid
    assert set(all_sand) == key_all_sand

    add_sand(grid, 1, 0)
    add_sand(grid, 1, 2)
    assert len(all_sand) == 4  # the two adds should have failed


@max_score(7.5)
@with_import('sand_oo', 'all_sand')
@with_import('sand_oo', 'remove_sand')
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_remove_sand(Grid, Sand, remove_sand, all_sand, monkeypatch):
    monkeypatch.setattr(Sand, '__repr__', lambda self: str(self))
    monkeypatch.setattr(Sand, '__hash__', lambda self: hash(str(self)))

    key_grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', None, None],
         [None, 'r', 's']]
    )
    key_all_sand = set(construct_all_sand_list(Sand, key_grid))

    grid = build_sandy_grid(
        Grid, Sand,
        [['s', 's', None],
         ['s', None, 's'],
         [None, 'r', 's']]
    )
    all_sand[:] = construct_all_sand_list(Sand, grid)

    remove_sand(grid, 0, 0)
    remove_sand(grid, 2, 1)

    assert grid == key_grid
    assert set(all_sand) == key_all_sand

    remove_sand(grid, 0, 2)
    remove_sand(grid, 1, 2)

    # the two removes should have failed
    assert len(all_sand) == 3
    assert grid.get(0, 2) is None
    assert grid.get(1, 2) == 'r'


@max_score(5)
@with_import('sand_oo', 'all_sand')
@with_import('sand_oo', 'do_whole_grid')
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_do_whole_grid_all_falling_rules(Grid, Sand, do_whole_grid, all_sand, monkeypatch):
    monkeypatch.setattr(Sand, '__repr__', lambda self: str(self))
    monkeypatch.setattr(Sand, '__hash__', lambda self: hash(str(self)))

    key = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None, None, None, None, None, None],
         ['r', 's', 'r', 's', 'r', 's', 'r', 's'],
         [None, 'r', None, None, None, 'r', None, None]]
    )
    key_all_sand = set(construct_all_sand_list(Sand, key))

    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None, None, 's', 's', 's', None],
         ['r', 's', 'r', None, 'r', None, 'r', None],
         [None, 'r', None, None, None, 'r', None, None]]
    )
    all_sand[:] = construct_all_sand_list(Sand, grid)

    do_whole_grid()
    assert grid == key
    assert set(all_sand) == key_all_sand


@max_score(5)
@with_import('sand_oo', 'all_sand')
@with_import('sand_oo', 'do_whole_grid')
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_do_whole_grid_sand_falls_together(Grid, Sand, do_whole_grid, all_sand, monkeypatch):
    monkeypatch.setattr(Sand, '__repr__', lambda self: str(self))
    monkeypatch.setattr(Sand, '__hash__', lambda self: hash(str(self)))

    key = build_sandy_grid(Grid, Sand, [[None], ['s'], ['s'], ['s'], ['s']])
    key_all_sand = set(construct_all_sand_list(Sand, key))

    grid = build_sandy_grid(Grid, Sand, [['s'], ['s'], ['s'], ['s'], [None]])
    all_sand[:] = construct_all_sand_list(Sand, grid)

    do_whole_grid()
    assert grid == key
    assert set(all_sand) == key_all_sand


@max_score(5)
@with_import('sand_oo', 'all_sand')
@with_import('sand_oo', 'do_whole_grid')
@with_import('sand_oo', 'Sand')
@with_import('Grid', 'Grid')
def test_do_whole_grid_until_sand_settles(Grid, Sand, do_whole_grid, all_sand, monkeypatch):
    monkeypatch.setattr(Sand, '__repr__', lambda self: str(self))
    monkeypatch.setattr(Sand, '__hash__', lambda self: hash(str(self)))

    key_grids = [
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             ['s', 's', None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             ['s', 's', 's']]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, 's', None],
             ['s', 's', None],
             ['s', 's', 's']]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, None, None],
             ['s', 's', 's'],
             ['s', 's', 's']]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, None, None],
             ['s', 's', 's'],
             ['s', 's', 's']]
        )
    ]

    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None]]
    )
    all_sand[:] = construct_all_sand_list(Sand, grid)

    for key in key_grids:
        key_all_sand = set(construct_all_sand_list(Sand, key))

        do_whole_grid()
        assert grid == key
        assert set(all_sand) == key_all_sand
