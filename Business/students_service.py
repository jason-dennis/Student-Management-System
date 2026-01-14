from Domain.student import Student
from Exceptions.error_add import ErrorAdd
from Validator.validator_student import ValidatorStudent
import random
import names


class StudentService:
    def __init__(self, repo_students, validator_student):
        self.repo_students = repo_students
        self.validator_student = validator_student

    def get_greater_than_5(self):
        """
        This function return the students with overall grade greater than 5
        :return:
        """
        students = self.repo_students.get_students_ordered_by_overall_grade_greater_than_5()
        return students

    def get_ordonated_by_name(self, subject):
        """
        This function return the students ordonated by name
        :return:
        """
        ordonated_by_name = self.repo_students.get_ordonated_by_name(subject)
        return ordonated_by_name

    def get_ordonated_by_grade(self, subject):
        """
        This function return the students ordonated by grade at a subject
        :return:
        """
        ordonated_by_grade = self.repo_students.get_ordonated_by_grade(subject)
        return ordonated_by_grade

    def get_top_20_students(self):
        """
        This function return the students top 20
        :return:
        """
        top_20_students = self.repo_students.get_top_20_students()
        return top_20_students

    def add_student(self, id, name):
        """
        This function adds a new student to the repo
        :param id:
        :param name:
        :return:
        """
        student = Student(id, name)
        self.validator_student.validate_student(student)
        self.repo_students.add_student(student)

    def modify_student_name(self, student, name):
        """
        This function modifies the student name in the repo
        :param id:
        :param name:
        :return:
        """
        student.set_name(name)

    def view_repository_students(self):
        """
        This function displays the repository subjects.
        :return:
        """
        return self.repo_students.get_all()

    def search_student_by_id(self, id_student):
        """
        This function searches the student by id.
        :param id_student:
        :return:
        """
        return self.repo_students.search_student_by_id(id_student)

    def search_student_by_name(self, id_student):
        """
        This function searches the student by id.
        :param id_student:
        :return:
        """
        return self.repo_students.search_student_by_name(id_student)

    def add_grade(self, student, subject, grade):
        """
        This function adds a new grade to the student.
        :param student:
        :param subject:
        :param grade:
        :return:
        """
        student.add_grade(subject, grade)

    def get_grade(self, student, subject):
        """
        This function returns the grade of the student.
        :param student:
        :param subject:
        :return:
        """
        return student.get_grade(subject)

    def generate_student(self):
        """
        This function generates a new student.
        :return:
        """
        student_name = names.get_full_name()
        while True:
            id_student = random.randint(1, 10000)
            student = Student(id_student, student_name)
            try:
                self.validator_student.validate_student(student)
                self.repo_students.add_student(student)
                break
            except (ErrorAdd, ValidatorStudent) as erorr:
                continue
