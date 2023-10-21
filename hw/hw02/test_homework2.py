from byuimage import Image
from byu_pytest_utils import max_score, test_files, with_import
import sys

sys.path.append(str(test_files))
import image_solutions  # nopep8


def assert_equal(observed: Image, expected: Image):
    assert observed.width == expected.width
    assert observed.height == expected.height
    for y in range(observed.height):
        for x in range(observed.width):
            observed_pixel = observed.get_pixel(x, y)
            expected_pixel = expected.get_pixel(x, y)
            assert observed_pixel.red == expected_pixel.red, f"the pixels at ({x}, {y}) don't match"
            assert observed_pixel.green == expected_pixel.green, f"the pixels at ({x}, {y}) don't match"
            assert observed_pixel.blue == expected_pixel.blue, f"the pixels at ({x}, {y}) don't match"


@max_score(10)
@with_import('homework2', 'flipped')
def test_flipped_with_landscape(flipped):
    observed = flipped(test_files / 'landscape.png')
    assert_equal(observed, image_solutions.landscape_flipped)


@max_score(10)
@with_import('homework2', 'flipped')
def test_flipped_with_flamingo_float(flipped):
    observed = flipped(test_files / 'flamingo-float.png')
    assert_equal(observed, image_solutions.flamingo_float_flipped)


@max_score(10)
@with_import('homework2', 'make_borders')
def test_make_borders_landscape(make_borders):
    observed = make_borders(test_files / 'landscape.png', 30, 0, 255, 0)
    assert_equal(observed, image_solutions.landscape_border)


@max_score(10)
@with_import('homework2', 'make_borders')
def test_make_borders_flamingo_float_10(make_borders):
    observed = make_borders(test_files / 'flamingo-float.png', 10, 0, 255, 255)
    assert_equal(observed, image_solutions.flamingo_float_border_10)


@max_score(10)
@with_import('homework2', 'make_borders')
def test_make_borders_flamingo_float_5(make_borders):
    observed = make_borders(
        test_files / 'flamingo-float.png', 5, 255, 125, 125)
    assert_equal(observed, image_solutions.flamingo_float_border_5)
