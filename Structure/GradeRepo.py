from Structure.Sorting import Sorter
class RepoGrade:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return self.grades

    def sort_grades(self):
        return Sorter.insertion_sort(self.grades, key=lambda g: (-g.grade, g.subject, g.student))
