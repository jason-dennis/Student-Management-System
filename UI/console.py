from Exceptions.UI_errors import UiError
from Exceptions.error_add import ErrorAdd
from Exceptions.validator_exceptions import ErrorValidator


class Console:
    def __init__(self, students_service, subject_service,grade_service):
        self.__RESET = "\033[0m"
        self.__GREEN = "\033[32m"
        self.__BLUE = "\033[38;5;75m"
        self.__PINK = "\033[38;5;205m"
        self.__YELLOW = "\033[38;5;228m"
        self.students_service = students_service
        self.subject_service = subject_service
        self.grade_service = grade_service
        self.__commands = {
            "add_student": self.add_student,
            "add_subject": self.add_subject,
            "view_subjects": self.view_subjects,
            "view_students": self.view_students,
            "delete_student": self.delete_student,
            "delete_subject": self.delete_subject,
            "generate_students": self.generate_students,
            "modify_student_name": self.modify_student_name,
            "modify_subject_name": self.modify_subject_name,
            "modify_subject_professor": self.modify_subject_professor,
            "search_student_by_name": self.search_student_by_name,
            "search_subject_by_name": self.search_subject_by_name,
            "assign_grade": self.assign_grade,
            "get_students_by_name": self.get_students_by_name,
            "get_students_by_subject_grade": self.get_students_by_subject_grade,
            "get_top_20": self.get_top_20,
            "get_greater_than_5":self.get_greater_than_5,
            "get_grades_sorted":self.get_grades_sorted
        }

    def get_grades_sorted(self,command_parameters):
        if len(command_parameters) != 0:
            raise UiError("Invalid number of parameters")
        repo=self.grade_service.sort_grades()
        for grade in repo:
            self.write_message(str(grade))


    def get_greater_than_5(self,command_parameters):
        """
        This function print students with overall grade greater than 5.
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 0:
            raise UiError("Invalid number of parameters")

        repo=self.students_service.get_greater_than_5()
        for student in repo:
            self.write_message(str(student) + " | " + str(student.overall_average()))

    def get_top_20(self, command_parameters):
        """
        This function print top 20%
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 0:
            raise UiError("Invalid number of parameters")
        top = self.students_service.get_top_20_students()
        for student in top:
            self.write_message(str(student) + " | " + str(student.overall_average()))

    def get_students_by_subject_grade(self, command_parameters):
        """
        This function return students ordered by subject grade.
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 1:
            raise UiError("Invalid numbers of parameters!")
        subject = command_parameters[0]
        ordonated_by_name = self.students_service.get_ordonated_by_grade(subject)
        for student in ordonated_by_name:
            self.write_message(str(student) + " | " + str(student.grade_for_subject(subject)))

    def get_students_by_name(self, command_parameters):
        """
        This function return students ordered by name.
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 1:
            raise UiError("Invalid numbers of parameters!")
        subject = command_parameters[0]
        ordonated_by_name = self.students_service.get_ordonated_by_name(subject)
        for student in ordonated_by_name:
            self.write_message(str(student) + " | " + str(student.grade_for_subject(subject)))

    def assign_grade(self, command_parameters):
        """
        This function assign a grade to the student
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 4:
            raise UiError("Invalid number of arguments")

        student_name = command_parameters[0] + " " + command_parameters[1]
        subject_name = command_parameters[2]
        grade = command_parameters[3]
        student = self.students_service.search_student_by_name(student_name)
        subject = self.subject_service.search_subject_by_name(subject_name)
        if student is None:
            raise UiError("Student not found")
        elif subject is None:
            raise UiError("Subject not found")
        else:
            self.students_service.add_grade(student, subject_name, grade)
            self.grade_service.add_grade(int(grade), subject_name, student_name)

    def modify_student_name(self, command_parameters):
        if len(command_parameters) != 2:
            raise UiError("Invalid numbers of parameters!")
        try:
            id_student = int(command_parameters[0])
        except ValueError:
            raise UiError("ID not an integer!")
        student = self.students_service.search_student_by_id(id_student)
        if student is None:
            raise UiError("Student not found!")
        else:
            self.students_service.modify_student_name(student, command_parameters[1])

    def modify_subject_name(self, command_parameters):
        """
        This function modify subject name.
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 2:
            raise UiError("Invalid numbers of parameters!")
        try:
            id_subject = int(command_parameters[0])
        except ValueError:
            raise UiError("ID not an integer!")
        subject = self.subject_service.search_subject_by_id(id_subject)
        if subject is None:
            raise UiError("Student not found!")
        else:
            self.subject_service.modify_subject_name(subject, command_parameters[1])

    def modify_subject_professor(self, command_parameters):
        """
        This function modify subject professor.
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 2:
            raise UiError("Invalid numbers of parameters!")
        try:
            id_subject = int(command_parameters[0])
        except ValueError:
            raise UiError("ID not an integer!")
        subject = self.subject_service.search_subject_by_id(id_subject)
        if subject is None:
            raise UiError("Subject not found!")
        else:
            self.subject_service.modify_subject_professor(subject, command_parameters[1])

    def search_student_by_name(self, command_parameters):
        """
        This function search student by name.
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 2:
            raise UiError("Invalid numbers of parameters!")

        name = command_parameters[0] + " " + command_parameters[1]
        student = self.students_service.search_student_by_name(name)
        if student is None:
            raise UiError("Student not found!")
        else:
            self.write_message(str(student))

    def search_subject_by_name(self, command_parameters):
        """
        This function search subject by name.
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 1:
            raise UiError("Invalid numbers of parameters!")

        subject = self.subject_service.search_subject_by_name(command_parameters[0])
        if subject is None:
            raise UiError("Subject not found!")
        else:
            self.write_message(str(subject))

    def generate_students(self, command_parameters):
        """
        This function generates the n students 
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 1:
            raise UiError("Invalid numbers of parameters!")

        number = int(command_parameters[0])
        while number > 0:
            self.students_service.generate_student()
            number -= 1

    def delete_student(self, command_parameters):
        """
        This function delete the student that user introduce
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 1:
            raise UiError("Invalid numbers of parameters!")

        try:
            id_student = int(command_parameters[0])
        except ValueError:
            raise UiError("ID not an integer!")
        student = self.students_service.search_student_by_id(id_student)
        if student is None:
            raise UiError("Student not found!")
        else:
            student.set_deleted(True)

    def delete_subject(self, command_parameters):
        """
        This function delete the student that user introduce
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 1:
            raise UiError("Invalid numbers of parameters!")

        try:
            id_student = int(command_parameters[0])
        except ValueError:
            raise UiError("ID not an integer!")
        subject = self.subject_service.search_subject_by_id(id_student)
        if subject is None:
            raise UiError("Subject not found!")
        else:
            subject.set_deleted(True)

    def view_subjects(self, command_parameters):
        """
        This function print all subjects
        :return:
        """
        repo = self.subject_service.view_repository_subjects()
        for subject in repo:
            if not subject.is_deleted():
                self.write_message(str(subject))

    def view_students(self, command_parameters):
        """
        This function prints all students
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 0:
            raise UiError("Invalid numbers of parameters!")
        repo = self.students_service.view_repository_students()
        for student in repo:
            if not student.is_deleted():
                self.write_message(str(student))

    def add_student(self, command_parameters):
        """
        This function add the student that user introduce
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 3:
            raise UiError("Invalid numbers of parameters!")

        try:
            id_student = int(command_parameters[0])
        except ValueError:
            raise UiError("ID not an integer!")

        name_student = command_parameters[1] + " " + command_parameters[2]
        try:
            self.students_service.add_student(id_student, name_student)
        except (ErrorAdd, ErrorValidator) as error:
            raise UiError(error)

    def add_subject(self, command_parameters):
        """
        This function add the subject that user introduce
        :param command_parameters:
        :return:
        """
        if len(command_parameters) != 3:
            raise UiError("Invalid numbers of parameters!")

        try:
            id_subject = int(command_parameters[0])
        except ValueError:
            raise UiError("ID not an integer!")
        name = command_parameters[1]
        professor = command_parameters[2]

        try:
            self.subject_service.add_subject(id_subject, name, professor)
        except (ErrorAdd, ErrorValidator) as error:
            raise UiError(error)

    def run_console(self):
        """
        This function runs the app
        :return:
        """
        while True:
            text_command = self.read_command()
            if text_command == "":
                continue
            if text_command == "exit":
                self.write_message("Good Bye Sir !!")
                return
            commands = text_command.split()
            command_name = commands[0]
            if command_name in self.__commands:
                command_parameters = commands[1:]
                try:
                    self.__commands[command_name](command_parameters)
                except UiError as error:
                    self.write_message(error)

    def read_command(self):
        """
        This function read a command from the console.
        :return:
        """
        command = input(
            f"{self.__BLUE}{"➜ "}{self.__PINK}{" GradeBook "}{self.__YELLOW}{"✗ "}{self.__GREEN}"
        ).strip()
        return command

    def write_message(self, message):
        print(f"{self.__RESET}{message}")

    def run_command(self, command):
        pass
