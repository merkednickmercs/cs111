
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


def convert_row_type(numbers):
    converted_row = []
    for row in numbers:
        row = float(row)
        converted_row.append(row)
    return converted_row


def calculate_score(scores):
    sat = scores[0]
    gpa = scores[1]
    interest = scores[2]
    strength = scores[3]
    calculated_score = ((sat / 160) * 0.3) + ((gpa * 2) * 0.4) + (interest * 0.1) + (strength * 0.2)
    return calculated_score

def is_outlier(scores):
    if scores[2] == 0 or (scores[1] * 2) - (scores[0] / 160) > 2:
        return True 
    else:
        return False

def calculate_score_improved (calculated_score, outliers):
    if calculated_score >= 6 or outliers is True:
        return True 
    else:
        return False

def grade_outlier (grades):
    sorted_grades = sorted(grades)
    if sorted_grades[1] - sorted_grades[0] > 20:
        return True    
    else:
        return False
    
def grade_improvement(grades):
    if grades == sorted (grades) :
        return True 
    else:
        return False
    
    print("done!")

def main():
        input_file = open("superheroes_tiny.csv", "r")
        student_scores_file = open("student_scores.csv", 'w')
        chosen_students_file = open("chosen_students.txt", "w")
        outliers_file = open("outliers.txt", "w")
        chosen_improved_file = open("chosen_improved.txt", "w")
        improved_chosen_file = open("improved_chosen.csv", "w")
        eic_file = open("extra_improved_chosen.txt", "w")
        # grab the line with the headers
        input_file.readline()
        # TODO: Loop through the rest of the file

        for line in input_file.readlines():
            individual = line.split(',')
            student_name = individual[0]
            numbers = individual[1:]
            converted_list = convert_row_type(numbers) 
            check_row_types (converted_list)
            if check_row_types (converted_list) is False:
                print("Error- wrong row type")
            scores = converted_list[:4]
            grades = converted_list[4:]
            calculated_score = calculate_score(scores)
            student_scores_file.write(f'{student_name},{calculated_score:.2f}\n')
            if calculated_score >= 6:
                chosen_students_file.write(f'{student_name}\n')

            outliers = is_outlier (scores)

            if outliers is True:
                outliers_file.write(f'{student_name}\n')

            if calculated_score >= 6 or (outliers and calculated_score >= 5):
                chosen_improved_file.write(f'{student_name}\n')
            if calculate_score_improved (calculated_score, outliers) is True:
                improved_chosen_file.write(f'{student_name},{scores[0]},{scores[1]},{scores[2]},{scores[3]}\n')
            if calculated_score >= 6 or (calculated_score >= 5 and (outliers or grade_outlier (grades) or grade_improvement (grades))):
                eic_file.write(f'{student_name}\n')
        # TODO: make sure to close all files you've opened!

        input_file.close()
        student_scores_file.close()
        chosen_students_file.close()
        outliers_file.close()
        chosen_improved_file.close()
        improved_chosen_file.close()
        eic_file.close()

        print("done!")

if __name__ == "__main__":
    main()