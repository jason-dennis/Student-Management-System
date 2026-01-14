from Exceptions.error_add import ErrorAdd
from Domain.student import Student
from Structure.Sorting import Sorter

class FileRepoStudents:

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__students_repo = []
        self.__load_from_file()

    def __ensure_file_exists(self):
        """
        This function check the file exist
        :return:
        """
        try:
            with open(self.__file_path, "a", encoding="utf-8"):
                pass
        except OSError as e:
            raise ErrorAdd(f"Cannot open students file: {e}")

    def __load_from_file(self):
        """
        This function load from file
        :return:
        """
        self.__ensure_file_exists()
        self.__students_repo.clear()

        with open(self.__file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = [p.strip() for p in line.split(";")]
                if len(parts) < 2:
                    continue

                id_student = int(parts[0])
                name = parts[1]
                deleted = False
                if len(parts) >= 3:
                    deleted = bool(int(parts[2]))

                st = Student(id_student, name)
                st.set_deleted(deleted)
                self.__students_repo.append(st)

    def __save_to_file(self):
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for st in self.__students_repo:
                deleted_flag = 1 if st.is_deleted() else 0
                f.write(f"{st.get_id_student()};{st.get_name()}\n")

    def __len__(self):
        return len(self.__students_repo)

    def add_student(self, student):
        """
        This method add a student to repo
        :param student:
        :return:
        """
        id_student = student.get_id_student()
        student.set_deleted(False)

        if any(stud.get_id_student() == id_student for stud in self.__students_repo):
            raise ErrorAdd("There is already a student with this ID")

        self.__students_repo.append(student)
        self.__save_to_file()

    def __len__(self):
        """
        This function returns the number of students.
        :return:
        """
        return len(self.__students_repo)

    def get_ordonated_by_name(self, subject):
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

        return Sorter.comb_sort(filtered, key=lambda s: s._Student__data["name"])

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
        return Sorter.insertion_sort(
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
        active = [s for s in self.__students_repo if not s._Student__data["deleted"] and s.overall_average() >= 5]
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

    def search_student_by_name(self, name):
        """
        This function searches for student by name.
        :param name:
        :return:
        """

        for student in self.__students_repo:
            if student.get_name() == name and not student.is_deleted():
                return student
        return None

    def search_student_by_id(self, id):
        """
        This function searches for student by id.
        :param id:
        :return:
        """
        for student in self.__students_repo:
            if student.get_id_student() == id and not student.is_deleted():
                return student

        return None

    def get_all(self):
        return self.__students_repo
