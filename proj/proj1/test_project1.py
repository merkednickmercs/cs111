from byuimage import Image
from byu_pytest_utils import max_score, run_python_script, test_files
import functools
import pytest


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


@max_score(20)
def test_display_image(monkeypatch):
    observed = None

    @functools.wraps(Image.show)
    def patched_Image_show(self):
        nonlocal observed
        observed = self
    monkeypatch.setattr(Image, 'show', patched_Image_show)

    run_python_script('image_processing.py', '-d',
                      test_files / 'explosion.input.jpg')

    if observed is None:
        pytest.fail('No Image was shown')

    assert_equal(observed, Image(test_files / 'explosion.input.jpg'))


def make_filter_tester(observed_file, key_file, *script_args):
    def decorator(func):
        @functools.wraps(func)
        def inner_func():
            run_python_script('image_processing.py', *script_args)
            assert_equal(Image(observed_file), Image(key_file))
        return inner_func
    return decorator


@max_score(5)
@make_filter_tester(
    'darkened-explosion.output.jpg', test_files / 'darkened-explosion.key.jpg',
    '-k', test_files / 'explosion.input.jpg', 'darkened-explosion.output.jpg', 0.3
)
def test_darken_filter():
    ...


@max_score(5)
@make_filter_tester(
    'sepia-explosion.output.jpg', test_files / 'sepia-explosion.key.jpg',
    '-s', test_files / 'explosion.input.jpg', 'sepia-explosion.output.jpg'
)
def test_sepia_filter():
    ...


@max_score(5)
@make_filter_tester(
    'grayscale-explosion.output.jpg', test_files / 'grayscale-explosion.key.jpg',
    '-g', test_files / 'explosion.input.jpg', 'grayscale-explosion.output.jpg'
)
def test_grayscale_filter():
    ...


@max_score(5)
@make_filter_tester(
    'bordered-explosion.output.jpg', test_files / 'bordered-explosion.key.jpg',
    '-b', test_files / 'explosion.input.jpg', 'bordered-explosion.output.jpg', 10, 120, 20, 14
)
def test_border_filter():
    ...


@max_score(5)
@make_filter_tester(
    'flipped-explosion.output.jpg', test_files / 'flipped-explosion.key.jpg',
    '-f', test_files / 'explosion.input.jpg', 'flipped-explosion.output.jpg'
)
def test_flip_filter():
    ...


@max_score(15)
@make_filter_tester(
    'mirrored-explosion.output.jpg', test_files / 'mirrored-explosion.key.jpg',
    '-m', test_files / 'explosion.input.jpg', 'mirrored-explosion.output.jpg'
)
def test_mirror_filter():
    ...


@max_score(20)
@make_filter_tester(
    'collage.output.jpg', test_files / 'collage.key.jpg',
    '-c', test_files / 'beach1.input.jpg', test_files / 'beach2.input.jpg',
    test_files / 'beach3.input.jpg', test_files / 'beach4.input.jpg',
    'collage.output.jpg', 10
)
def test_collage_filter():
    ...


@max_score(20)
@make_filter_tester(
    'greenscreen.output.jpg', test_files / 'greenscreen.key.jpg',
    '-y', test_files / 'man.input.jpg', test_files / 'explosion.input.jpg',
    'greenscreen.output.jpg', 90, 1.3
)
def test_greenscreen_filter():
    ...
