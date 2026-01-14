from Tests.tests import Tests
from UI.console import Console
from Validator.validator_student import ValidatorStudent
from Validator.validator_subjects import ValidatorSubjects
from Structure.students import RepoStudents
from Structure.RepoSubjects import RepoSubjects
from Business.students_service import StudentService
from Business.subject_service import SubjectService
from Structure.FileRepoSubject import FileRepoSubjects
from Structure.FileRepoStudent import FileRepoStudents
from Business.grade_service import GradeService
from Structure.GradeRepo import RepoGrade
from Structure.FileRepGrade import FileGradeRepo
USE_FILES = True

if USE_FILES:
    repo_student = FileRepoStudents("students.txt")
    repo_subject = FileRepoSubjects("subjects.txt")
else:
    repo_student = RepoStudents()
    repo_subject = RepoSubjects()

validator_student = ValidatorStudent()
validator_subject = ValidatorSubjects()


student_service = StudentService(repo_student, validator_student)
subject_service = SubjectService(repo_subject, validator_subject)
if USE_FILES:
    repo_grade = FileGradeRepo("grades.txt",student_service,subject_service)
else:
    repo_grade = RepoGrade()

grade_service = GradeService(repo_grade)

tests = Tests()
tests.run_tests()
console = Console(student_service,subject_service,grade_service)
console.run_console()

# assign_grade Dennis Ognean Analiza 10
# assign_grade Paul Luput Analiza 9
# assign_grade Dennis Ognean Analiza 9
# assign_grade Dennis Ognean Fp 10
# assign_grade Paul Luput Fp 10
# assign_grade Paul Luput Fp 7
# get_grades_sorted