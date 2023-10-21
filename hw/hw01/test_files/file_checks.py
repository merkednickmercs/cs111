"""
MAKE SURE THIS PROGRAM IS IN THE SAME FOLDER AS THE KEY FILES 
AND THE FILES OUTPUTTED BY YOUR PROGRAM
"""

def check_file(student_filename):
    key_filename = "test_files/key_" + student_filename
    with open(key_filename) as key_file, open(student_filename) as student_file:
        student_file_lines = student_file.readlines()
        key_file_lines = key_file.readlines()

    print(f"Checking {student_filename}...")
    is_same = True

    if len(student_file_lines) != len(key_file_lines):
        print("LINE COUNT DIFFERS: additional or missing students")
        is_same = False

    for expected_student in key_file_lines:
        if expected_student not in student_file_lines:
            print(f"Missing or bad formatting: {expected_student}", end="")
            is_same = False

    if is_same:
        print(f"{student_filename} is CORRECT\n--------------------------------------")  
    else:
        print(f"{student_filename} is INCORRECT\n--------------------------------------")


def run_checks(ans):
    if ans == 0 or ans == 6:
        check_file("chosen_students.txt")
    if ans == 1 or ans == 6:
        check_file("student_scores.csv")
    if ans == 2 or ans == 6:
        check_file("outliers.txt")
    if ans == 3 or ans == 6:
        check_file("chosen_improved.txt")
    if ans == 4 or ans == 6:
        check_file("improved_chosen.csv")
    if ans == 5 or ans == 6:    
        check_file("extra_improved_chosen.txt")


if __name__ == "__main__":
    print("""Enter a number for the file you want to check:
    (0) chosen_students.txt
    (1) student_scores.csv
    (2) outliers.txt
    (3) chosen_improved.txt
    (4) improved_chosen.csv
    (5) extra_improved_chosen.txt
    (6) run all checks""")
    ans = int(input("> "))
    run_checks(ans)
