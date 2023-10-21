from byu_pytest_utils import dialog, max_score, test_files


@max_score(3)
@dialog(test_files / 'no_flags.dialog.txt', 'lab05.py', 'CS', '111', 'Rocks!')
def test_no_flags():
    ...


@max_score(3)
@dialog(test_files / 'p_flag.dialog.txt', 'lab05.py', '-p', '1', '2', '3')
def test_p_flag():
    ...


@max_score(2)
@dialog(test_files / 'i_flag.dialog.txt', 'lab05.py', '-i')
def test_i_flag():
    ...


@max_score(3)
@dialog(test_files / 'h_flag.dialog.txt', 'lab05.py', '-h')
def test_h_flag():
    ...


@max_score(3)
@dialog(test_files / 'w_flag_with_no_content.dialog.txt', 'lab05.py', '-w', 'w_flag.output.txt')
def test_w_flag_with_no_content():
    ...


@max_score(3)
@dialog(
    test_files / 'w_flag_with_content.dialog.txt',
    'lab05.py', '-w', 'w_flag.output.txt', 'a', 'b', 'c', 'd',
    output_file='w_flag.output.txt'
)
def test_w_flag_with_content():
    ...


@max_score(3)
@dialog(test_files / 'r_flag.dialog.txt', 'lab05.py', '-r', test_files / 'r_flag.input.txt')
def test_r_flag():
    ...
