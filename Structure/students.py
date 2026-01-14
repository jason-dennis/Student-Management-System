from Exceptions.error_add import ErrorAdd
from Structure.Sorting import Sorter

class RepoStudents:
    def __init__(self):
        self.__students_repo = []

    def __len__(self):
        """
        This function returns the number of students.
        :return:
        """
        return len(self.__students_repo)


    def get_ordonated_by_name(self,subject):
        """
        This function returns the students ordered by name.
        :return:
        """
        filtered = [
            s for s in self.__students_repo
            if not s._Student__data["deleted"]
               and subject in s._Student__data["grades"]
               and len(s._Student__data["grades"][subject]) > 0
        ]

        return Sorter.insertion_sort(filtered, key=lambda s: s._Student__data["name"])

    def get_ordonated_by_grade(self, subject):
        """
        This function returns the students ordered by grade.
        :param subject:
        :return:
        """
        filtered = [
            s for s in self.__students_repo
            if not s._Student__data["deleted"]
               and subject in s._Student__data["grades"]
               and len(s._Student__data["grades"][subject]) > 0
        ]
        return Sorter.comb_sort(
            filtered,
            key=lambda s: s.grade_for_subject(subject),
            reverse=True
        )

    def get_students_ordered_by_overall_grade(self):
        """
        This function returns the students ordered by overall grade.
        :return:
        """
        active = [s for s in self.__students_repo if not s._Student__data["deleted"]]
        return Sorter.insertion_sort(active, key=lambda s: s.overall_average(), reverse=True)

    def get_students_ordered_by_overall_grade_greater_than_5(self):
        """
        This function returns the students ordered by overall grade.
        :return:
        """
        active = [s for s in self.__students_repo if not s._Student__data["deleted"] and s.overall_average()>=5]
        return Sorter.comb_sort(active, key=lambda s: s.overall_average(), reverse=True)
    def get_top_20_students(self):
        """
        This function returns the top 20 students.
        :return:
        """
        ordered = self.get_students_ordered_by_overall_grade()
        if not ordered:
            return []
        n = max(1, int(len(ordered) * 0.2))
        return ordered[:n]

    def add_student(self, student):
        """
        This function adds a student to the students list.
        :param student:
        :return:
        """
        id_student = student.get_id_student()
        student.set_deleted(False)
        if any(stud.get_id_student() == id_student for stud in self.__students_repo):
            raise ErrorAdd("There is already a student with this ID")
        self.__students_repo.append(student)


    #######recursiv######
    def search_student_by_name(self, name,index=0):
        """
        This function searches for student by name.
        :param name:
        :return:
        """
        if index >= len(self.__students_repo):
            return None

        student = self.__students_repo[index]

        if student.get_name() == name and not student.is_deleted():
            return student
        return self.search_student_by_id(id, index + 1)

    def search_student_by_id(self, id, index=0):
        """
        This function searches for student by id (recursive).
        :param id:
        :param index:
        :return:
        """
        if index >= len(self.__students_repo):
            return None

        student = self.__students_repo[index]

        if student.get_id_student() == id and not student.is_deleted():
            return student
        return self.search_student_by_id(id, index + 1)


    def get_all(self):
        return self.__students_repo
