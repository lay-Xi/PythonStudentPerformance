import json
import os
from re import sub
from student import Student

NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

def get_average_student_mark(student_data):
    total_student_averages = 0

    for student in student_data:
        total_student_averages += student.get_average()
    
    return round(total_student_averages / NUM_STUDENTS, 2)

def _get_subject_averages(student_data):
    subject_average_totals = {}
    subject_averages = {}

    for student in student_data:
        subject_average_totals["math"] = subject_average_totals.get("math", 0) + student.math
        subject_average_totals["science"] = subject_average_totals.get("science", 0) + student.science
        subject_average_totals["history"] = subject_average_totals.get("history", 0) + student.history
        subject_average_totals["english"] = subject_average_totals.get("english", 0) + student.english
        subject_average_totals["geography"] = subject_average_totals.get("geography", 0) + student.geography

    for subject, average in subject_average_totals.items():
        subject_averages[subject] = average / NUM_STUDENTS

    return dict(sorted(subject_averages.items(), key= lambda subject: subject[1]))

def _get_grade_averages(student_data):
    grade_average_totals = {}
    grade_student_count = {}
    grade_averages = {}

    for student in student_data:
        grade_average_totals[student.grade] = grade_average_totals.get(student.grade, 0) + student.get_average()
        grade_student_count[student.grade] = grade_student_count.get(student.grade, 0) + 1

    for grade, average in grade_average_totals.items():
        grade_averages[grade] = average / grade_student_count[grade]

    return dict(sorted(grade_averages.items(), key= lambda grade: grade[1]))

def get_hardest_subject(student_data):
    subject_averages = _get_subject_averages(student_data)
    
    return list(subject_averages.keys())[0]

def get_easiest_subject(student_data):
    subject_averages = _get_subject_averages(student_data)
    
    return list(subject_averages.keys())[len(subject_averages) - 1]

def get_best_performing_grade(student_data):
    grade_averages = _get_grade_averages(student_data)

    return list(grade_averages.keys())[len(grade_averages) - 1]

def get_worst_performing_grade(student_data):
    grade_averages = _get_grade_averages(student_data)

    return list(grade_averages.keys())[0]

def get_best_student(student_data):
    high_score = 0
    best_student = -1

    for student in student_data:
        if (student.get_average() > high_score):
            high_score = student.get_average()
            best_student = student.id

    return best_student

def get_worst_student(student_data):
    low_score = 100
    worst_student = -1

    for student in student_data:
        if (student.get_average() < low_score):
            low_score = student.get_average()
            worst_student = student.id
        
    return worst_student

def main():
    student_data = []

    for id in range(NUM_STUDENTS):
        student_data.append(Student(load_report_card("students", id)))

    print(f"Average Student Grade: {get_average_student_mark(student_data)}")
    print(f"Hardest Subject {get_hardest_subject(student_data)}")
    print(f"Easiest Subject: {get_easiest_subject(student_data)}")
    print(f"Best Performing Grade: {get_best_performing_grade(student_data)}")
    print(f"Worst Performing Grade: {get_worst_performing_grade(student_data)}")
    print(f"Best Student ID: {get_best_student(student_data)}")
    print(f"Worst Student ID: {get_worst_student(student_data)}")

if __name__ == "__main__":
    main()