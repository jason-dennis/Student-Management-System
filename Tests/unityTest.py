import unittest
import os

# --- IMPORTURI DOMAIN ---
from Domain.student import Student
from Domain.subject import Subject
from Domain.grade import Grade  # Am adaugat importul pentru Grade

# --- IMPORTURI VALIDATORI ---
from Validator.validator_student import ValidatorStudent
from Validator.validator_subjects import ValidatorSubjects

# --- IMPORTURI EXCEPTII ---
from Exceptions.validator_exceptions import ErrorValidator
from Exceptions.error_add import ErrorAdd

# --- IMPORTURI REPO MEMORIE ---
from Structure.students import RepoStudents
from Structure.RepoSubjects import RepoSubjects

# --- IMPORTURI REPO FISIERE (NOI) ---
# Asigura-te ca numele fisierelor sunt corecte (ex: FileRepGrade vs FileGradeRepo)
from Structure.FileRepoStudent import FileRepoStudents
from Structure.FileRepoSubject import FileRepoSubjects
from Structure.FileRepGrade import FileGradeRepo


class TestDomainEntities(unittest.TestCase):
    # -------- black-box --------

    def test_create_student(self):
        st = Student(17, "Paul")
        self.assertEqual(17, st.get_id_student())
        self.assertEqual("Paul", st.get_name())

    def test_create_subject(self):
        sb = Subject(17, "Calculus", "Berinde")
        self.assertEqual(17, sb.get_id_subject())
        self.assertEqual("Calculus", sb.get_name())
        self.assertEqual("Berinde", sb.get_professor())

    def test_delete_student_flag(self):
        st = Student(1, "A")
        st.set_deleted(False)
        self.assertFalse(st.is_deleted())
        st.set_deleted(True)
        self.assertTrue(st.is_deleted())

    def test_delete_subject_flag(self):
        sb = Subject(1, "X", "Y")
        sb.set_deleted(False)
        self.assertFalse(sb.is_deleted())
        sb.set_deleted(True)
        self.assertTrue(sb.is_deleted())

    def test_modify_student_name(self):
        st = Student(1, "Paul")
        st.set_name("Dennis")
        self.assertEqual("Dennis", st.get_name())

    def test_modify_subject(self):
        sb = Subject(1, "Calculus", "Berinde")
        sb.set_name("Maths")
        self.assertEqual("Maths", sb.get_name())
        sb.set_professor("Rafiliu")
        self.assertEqual("Rafiliu", sb.get_professor())


class TestValidators(unittest.TestCase):
    # -------- black-box --------

    def setUp(self):
        self.validator_student = ValidatorStudent()
        self.validator_subject = ValidatorSubjects()

    def test_validate_student_ok(self):
        st = Student(17, "Paul")
        self.validator_student.validate_student(st)

    def test_validate_student_invalid(self):
        st_invalid = Student(-1, "")
        with self.assertRaises(ErrorValidator) as ctx:
            self.validator_student.validate_student(st_invalid)
        self.assertEqual("Invalid id\nInvalid name\n", str(ctx.exception))

    def test_validate_subject_ok(self):
        sb = Subject(17, "Calculus", "Berinde")
        self.validator_subject.validate_subjects(sb)

    def test_validate_subject_invalid(self):
        sb_invalid = Subject(-1, "", "B3rinde")
        with self.assertRaises(ErrorValidator) as ctx:
            self.validator_subject.validate_subjects(sb_invalid)
        self.assertEqual("invalid id\ninvalid name\ninvalid professor\n", str(ctx.exception))


class TestRepositoriesBlackBox(unittest.TestCase):

    def setUp(self):
        self.repo_students = RepoStudents()
        self.repo_subjects = RepoSubjects()

        self.student = Student(17, "Paul")
        self.subject = Subject(17, "Calculus", "Berinde")

    def test_add_student_and_duplicate(self):
        self.repo_students.add_student(self.student)
        self.assertEqual(1, len(self.repo_students))

        with self.assertRaises(ErrorAdd) as ctx:
            self.repo_students.add_student(self.student)
        self.assertEqual("There is already a student with this ID", str(ctx.exception))

    def test_add_subject_and_duplicate(self):
        self.repo_subjects.add_subject(self.subject)
        self.assertEqual(1, len(self.repo_subjects))

        with self.assertRaises(ErrorAdd) as ctx:
            self.repo_subjects.add_subject(self.subject)
        self.assertEqual("There is already a subject with this ID", str(ctx.exception))

    def test_search_by_name(self):
        self.repo_students.add_student(self.student)
        self.student.set_name("Dennis")

        self.repo_subjects.add_subject(self.subject)
        self.subject.set_name("Maths")

        self.assertIs(self.repo_students.search_student_by_name("Dennis"), self.student)
        self.assertIsNone(self.repo_students.search_student_by_name("ION"))

        self.assertIs(self.repo_subjects.search_subject_by_name("Maths"), self.subject)
        self.assertIsNone(self.repo_subjects.search_subject_by_name("Calculus"))

    def test_search_by_id(self):
        self.repo_students.add_student(self.student)
        self.repo_subjects.add_subject(self.subject)

        self.assertIs(self.repo_students.search_student_by_id(17), self.student)
        self.assertIsNone(self.repo_students.search_student_by_id(15))

        self.assertIs(self.repo_subjects.search_subject_by_id(17), self.subject)
        self.assertIsNone(self.repo_subjects.search_subject_by_id(15))


class TestRepoStudentsWhiteBox(unittest.TestCase):

    def setUp(self):
        self.repo = RepoStudents()

    def _add_student_with_average(self, sid: int, name: str, avg: float):
        st = Student(sid, name)
        self.repo.add_student(st)
        # Hack rapid pentru a simula media fara a adauga note complete
        # Nota: intr-un test real de integrare ar trebui adaugate note prin service
        st.overall_average = lambda: avg
        return st

    def test_get_top_20_empty_repo(self):
        self.assertEqual([], self.repo.get_top_20_students())

    def test_get_top_20_single_student(self):
        st = self._add_student_with_average(1, "A", 9.0)
        top = self.repo.get_top_20_students()

        self.assertEqual(1, len(top))
        self.assertIs(top[0], st)

    def test_get_top_20_ten_students(self):
        students = []
        for i in range(10):
            students.append(self._add_student_with_average(i + 1, f"S{i + 1}", float(i)))

        top = self.repo.get_top_20_students()
        self.assertEqual(2, len(top))

        self.assertIs(top[0], students[9])
        self.assertIs(top[1], students[8])

    def test_get_top_20_rounding_down_behavior(self):
        students = []
        for i in range(6):
            students.append(self._add_student_with_average(i + 1, f"S{i + 1}", float(i)))

        top = self.repo.get_top_20_students()
        self.assertEqual(1, len(top))
        self.assertIs(top[0], students[5])


class TestFileRepositories(unittest.TestCase):
    """
    Testeaza persistenta datelor (FileRepoStudents, FileRepoSubjects, FileGradeRepo).
    Creeaza fisiere temporare la inceput si le sterge la final.
    """

    def setUp(self):
        # Numele fisierelor temporare
        self.file_student = "test_students_temp.txt"
        self.file_subject = "test_subjects_temp.txt"
        self.file_grade = "test_grades_temp.txt"

        # 1. Setup Student File (scriem un student initial manual)
        with open(self.file_student, "w") as f:
            f.write("1;Ion Popescu;0\n")

        # 2. Setup Subject File (o materie initiala)
        with open(self.file_subject, "w") as f:
            f.write("100;Matematica;Prof X;0\n")

        # 3. Setup Grade File (o nota initiala)
        with open(self.file_grade, "w") as f:
            f.write("9.5;Matematica;Ion Popescu\n")

    def tearDown(self):
        # Stergem fisierele create dupa rularea testelor
        if os.path.exists(self.file_student): os.remove(self.file_student)
        if os.path.exists(self.file_subject): os.remove(self.file_subject)
        if os.path.exists(self.file_grade): os.remove(self.file_grade)

    def test_file_student_repo_persistence(self):
        # 1. Testam incarcarea (Load)
        repo = FileRepoStudents(self.file_student)
        self.assertEqual(len(repo), 1)
        st = repo.search_student_by_id(1)
        self.assertEqual(st.get_name(), "Ion Popescu")

        # 2. Testam salvarea (Add & Save)
        new_st = Student(2, "Maria Ionescu")
        repo.add_student(new_st)
        self.assertEqual(len(repo), 2)

        # 3. Verificam persistenta (reincarcand repo-ul sau citind fisierul)
        repo_reload = FileRepoStudents(self.file_student)
        self.assertEqual(len(repo_reload), 2)
        found = repo_reload.search_student_by_id(2)
        self.assertEqual(found.get_name(), "Maria Ionescu")

    def test_file_subject_repo_persistence(self):
        # 1. Testam incarcarea
        repo = FileRepoSubjects(self.file_subject)
        self.assertEqual(len(repo), 1)
        sb = repo.search_subject_by_name("Matematica")
        self.assertEqual(sb.get_professor(), "Prof X")

        # 2. Testam salvarea
        new_sb = Subject(101, "Informatica", "Prof Y")
        repo.add_subject(new_sb)

        # 3. Verificam persistenta in fisierul fizic
        with open(self.file_subject, "r") as f:
            content = f.read()
            self.assertIn("101;Informatica;Prof Y", content)

    # def test_file_grade_repo_persistence(self):
    #     # 1. Testam incarcarea
    #     repo = FileGradeRepo(self.file_grade)
    #     self.assertEqual(len(repo), 1)
    #     grades = repo.get_grades()
    #     self.assertEqual(grades[0].grade, 9.5)
    #
    #     # 2. Testam salvarea
    #     new_grade = Grade(10.0, "Fizica", "Maria Ionescu")
    #     repo.add_grade(new_grade)
    #
    #     # 3. Verificam persistenta
    #     repo_reload = FileGradeRepo(self.file_grade)
    #     self.assertEqual(len(repo_reload), 2)
    #     # Verificam ultima nota adaugata
    #     last_grade = repo_reload.get_grades()[-1]
    #     self.assertEqual(last_grade.subject, "Fizica")
    #

if __name__ == "__main__":
    unittest.main()