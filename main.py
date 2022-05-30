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



def get_hardest_subject(student_data):
    subject_averages = _get_subject_averages(student_data)
    
    return list(subject_averages.keys())[0]

def get_easiest_subject(student_data):
    subject_averages = _get_subject_averages(student_data)
    
    return list(subject_averages.keys())[len(subject_averages) - 1]

def get_best_performing_grade(student_data):
    pass

def get_worst_performing_grade(student_data):
    pass

def get_best_student(student_data):
    pass

def get_worst_student(student_data):
    pass

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