class Grade:
    def __init__(self,grade,subject,student):
        self.grade = grade
        self.subject = subject
        self.student=student

    def __str__(self):
        return f'{self.grade}{" | "}{self.subject} |   {self.student}'

    def get_subject(self):
       return self.subject

    def get_grade(self):
       return self.grade

    def get_student(self):
        return self.student

    