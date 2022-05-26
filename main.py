import json
import os
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
    pass

def get_hardest_subject(student_data):
    pass

def get_easiest_subject(student_data):
    pass

def get_best_performing_grade(student_data):
    pass

def get_worst_performing_grade(student_data):
    pass

def get_best_student(student_data):
    pass

def get_worst_student(student_data):
    pass

student_data = []

for id in range(NUM_STUDENTS):
    student_data.append(Student(load_report_card("students", id)))

print(f"Average Student Grade: {get_average_student_mark(student_data):.2f}")
print(f"Hardest Subject {get_hardest_subject(student_data)}")
print(f"Easiest Subject: {get_easiest_subject(student_data)}")
print(f"Best Performing Grade: {get_best_performing_grade(student_data)}")
print(f"Worst Performing Grade: {get_worst_performing_grade(student_data)}")
print(f"Best Student ID: {get_best_student(student_data)}")
print(f"Worst Student ID: {get_worst_student(student_data)}")