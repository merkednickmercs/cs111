from byu_pytest_utils import run_python_script, this_folder, max_score, test_files
import filecmp
import pytest


@pytest.fixture(scope="module",autouse=True)
def run_program():
    script = this_folder / "admissions.py"
    run_python_script(script)
    
@max_score(15)
def test_student_scores():
    assert filecmp.cmp(test_files / "key_student_scores.csv", this_folder / "student_scores.csv")
    
@max_score(5)
def test_chosen_student():
    assert filecmp.cmp(test_files / "key_chosen_students.txt", this_folder / "chosen_students.txt")

@max_score(5)
def test_outliers():
    assert filecmp.cmp(test_files / "key_outliers.txt", this_folder / "outliers.txt")

@max_score(5)
def test_improved_chosen():
    assert filecmp.cmp(test_files / "key_improved_chosen.csv", this_folder / "improved_chosen.csv")

@max_score(5)
def test_chosen_improved():
    assert filecmp.cmp(test_files / "key_chosen_improved.txt", this_folder / "chosen_improved.txt")

@max_score(15)
def test_extra_improved_chosen():
    assert filecmp.cmp(test_files / "key_extra_improved_chosen.txt", this_folder / "extra_improved_chosen.txt")


  