from Domain.student import Student
from Validator.validator_student import ValidatorStudent
from Validator.validator_subjects import ValidatorSubjects
from Exceptions.validator_exceptions import ErrorValidator
from Structure.students import RepoStudents
from Domain.subject import Subject
from Structure.RepoSubjects import RepoSubjects
from Exceptions.error_add import ErrorAdd


class Tests:
    def run_tests(self):
        """
        This function runs the tests
        :return:
        """
        repo_students = RepoStudents()
        repo_subject = RepoSubjects()
        student = self.test_create_student()
        subject = self.test_create_subject()
        self.test_validate_student(student)
        self.test_add_student(student, repo_students)
        self.test_validate_subject(subject)
        self.test_add_subject(subject, repo_subject)
        self.test_detele_student(student)
        self.test_delete_subject(subject)
        self.test_modify_student(student)
        self.test_modify_subject(subject)
        self.test_search_by_name(repo_students, repo_subject, student, subject)
        self.test_search_by_id(repo_students, repo_subject, student, subject)

    def test_create_student(self):
        """
        This function test the create student function
        :return:
        """
        id_student = 17
        name = "Paul"
        student = Student(id_student, name)
        assert (id_student == student.get_id_student())
        assert (name == student.get_name())

        return student

    def test_create_subject(self):
        """
        This function test the create subject function
        :return:
        """
        id_subject = 17
        name = "Calculus"
        professor = "Berinde"
        subject = Subject(id_subject, name, professor)
        assert (id_subject == subject.get_id_subject())
        assert (name == subject.get_name())
        assert (professor == subject.get_professor())
        return subject

    def test_validate_student(self, student):
        """
        This function test the validate student function
        :param student:
        :return:
        """
        validator_student = ValidatorStudent()
        validator_student.validate_student(student)

        id_invalid = -1
        nume_invalid = ""
        student_invalid = Student(id_invalid, nume_invalid)
        try:
            validator_student.validate_student(student_invalid)
            assert False
        except ErrorValidator as errors:
            assert str(errors) == "Invalid id\nInvalid name\n"

    def test_validate_subject(self, subject):
        """
        This function test the validate subject function
        :param subject:
        :return:
        """
        validator_subject = ValidatorSubjects()
        validator_subject.validate_subjects(subject)
        id_invalid = -1
        nume_invalid = ""
        professor_invalid = "B3rinde"
        subject_invalid = Subject(id_invalid, nume_invalid, professor_invalid)

        try:
            validator_subject.validate_subjects(subject_invalid)
            assert False
        except ErrorValidator as errors:
            assert str(errors) == "invalid id\ninvalid name\ninvalid professor\n"

    def test_add_student(self, student, repo_students):
        """
            This function test the add student function
        :param student:
        :return:
        """
        repo_students.add_student(student)
        assert len(repo_students) == 1
        try:
            repo_students.add_student(student)
            assert False
        except ErrorAdd as error:
            assert str(error) == "There is already a student with this ID"

    def test_add_subject(self, subject, repo_subject):
        """
        This function test the add subject function
        :param subject:
        :return:
        """
        repo_subject.add_subject(subject)
        assert len(repo_subject) == 1
        try:
            repo_subject.add_subject(subject)
            assert False
        except ErrorAdd as error:
            assert str(error) == "There is already a subject with this ID"

    def test_detele_student(self, student):
        """
        This function test the detele student function
        :param student:
        :return:
        """
        assert not student.is_deleted()
        student.set_deleted(True)
        assert student.is_deleted()
        student.set_deleted(False)

    def test_delete_subject(self, subject):
        """
        This function test the delete subject function
        :param subject:
        :return:
        """
        assert not subject.is_deleted()
        subject.set_deleted(True)
        assert subject.is_deleted()
        subject.set_deleted(False)

    def test_modify_student(self, student):
        """
        This function test the modify student function
        :param student:
        :return:
        """
        student.set_name("Dennis")
        assert (student.get_name() == "Dennis")

    def test_modify_subject(self, subject):
        """
        This function test the modify subject function
        :param subject:
        :return:
        """

        subject.set_name("Maths")
        assert (subject.get_name() == "Maths")
        subject.set_professor("Rafiliu")
        assert (subject.get_professor() == "Rafiliu")

    def test_search_by_name(self, repo_students, repo_subject, student, subject):
        """
        This function test the search by name function
        :param repo_students: 
        :param repo_subject: 
        :return: 
        """
        assert (repo_students.search_student_by_name("Dennis") == student)
        assert (repo_students.search_student_by_name("ION") == None)

        assert (repo_subject.search_subject_by_name("Maths") == subject)
        assert (repo_subject.search_subject_by_name("Calculus") == None)

    def test_search_by_id(self, repo_students, repo_subject, student, subject):
        """
        This function test the search by id function
        :param repo_students:
        :param repo_subject:
        :param student:
        :param subject:
        :return:
        """
        assert (repo_students.search_student_by_id(17) == student)
        assert (repo_students.search_student_by_id(15) == None)

        assert (repo_subject.search_subject_by_id(17) == subject)
        assert (repo_subject.search_subject_by_id(15) == None)
