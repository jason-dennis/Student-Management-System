from Domain.grade import Grade
class GradeService:
    def __init__(self,repo):
        self.repo = repo

    def add_grade(self,nota,subject,student):
        grade=Grade(nota,subject,student)
        self.repo.add_grade(grade)

    def sort_grades(self):
        list=self.repo.sort_grades()
        return list