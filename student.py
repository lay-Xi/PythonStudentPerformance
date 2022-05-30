class Student:
    def __init__(self, report_card):
        self.id = report_card["id"]
        self.grade = report_card["grade"]
        self.math = report_card["math"]
        self.science = report_card["science"]
        self.history = report_card["history"]
        self.english = report_card["english"]
        self.geography = report_card["geography"]
    
    def get_average(self):
        return (self.math + self.science + self.history + self.english + self.geography) / 5

    