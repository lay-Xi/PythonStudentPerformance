from main import get_average_student_mark, get_hardest_subject, get_easiest_subject, get_best_performing_grade, get_worst_performing_grade, get_best_student, get_worst_student
import json
import os
from student import Student

NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]

def _load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

student_data = []

for id in range(NUM_STUDENTS):
    student_data.append(Student(_load_report_card("students", id)))

def test_average_student_mark():
    assert get_average_student_mark(student_data) == 50.44

def test_hardest_subject():
    assert get_hardest_subject(student_data) == "geography"

def test_easiest_subject():
    assert get_easiest_subject(student_data) == "english"

def test_best_performing_grade():
    assert get_best_performing_grade(student_data) == 6

def test_worst_performing_grade():
    assert get_worst_performing_grade(student_data) == 5

def test_best_student():
    assert get_best_student(student_data) == 549

def test_worst_student():
    assert get_worst_student(student_data) == 637