from collections import defaultdict
class Student:
    def __init__(self, id_student, name):
        """
        The function create a student
        :param id_student: int
        :param name: string
        """
        self.__data = {
            "id_student": id_student,
            "name": name,
            "deleted": True,
            "grades": defaultdict(list)
        }
    def __str__(self):
        """
        This function returns a string representation of the student
        :return:
        """
        return f"{self.__data["id_student"]} | {self.__data["name"]} "
    def get_id_student(self):
        """
        This function returns the id_student of the student
        :return:
        """
        return self.__data["id_student"]

    def get_name(self):
        """
        This function returns the name of the student
        :return:
        """
        return self.__data["name"]

    def is_deleted(self):
        """
        This function returns whether the student is deleted
        :return:
        """
        return self.__data["deleted"]

    def set_deleted(self, deleted):
        """
        This function sets whether the student is deleted
        :param deleted:
        :return:
        """
        self.__data["deleted"] = deleted

    def set_name(self, name):
        """
        This function sets the name of the student
        :param name:
        :return:
        """
        self.__data["name"] = name

    def add_grade(self, subject, grade):
        """
        This function adds a grade to the student
        :param grade:
        :return:
        """
        self.__data["grades"][subject].append(grade)

    def get_grades(self, subject):
        """
        This function returns the grades of the student
        :param subject:
        :return:
        """
        return self.__data["grades"][subject]

    def grade_for_subject(self, subject):
        """
        This function returns the grades of the student
        :param subject:
        :return:
        """
        grades = self.__data["grades"][subject]
        int_grades=[int(grade) for grade in grades]
        return sum(int_grades) / len(int_grades) if grades else 0

    def overall_average(self):
        """
        This function returns the overall average of the student
        :return:
        """
        all_grades = []
        for grades in self.__data["grades"].values():
            all_grades.extend(int(grade) for grade in grades)

        return sum(all_grades) / len(all_grades) if all_grades else 0