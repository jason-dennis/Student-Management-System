from Domain.grade import Grade  # Asigură-te că importul este corect
from Structure.Sorting import Sorter


class FileGradeRepo:
    def __init__(self, file_path: str,students_service,subject_service):
        # Inițializăm lista manual (fără super, conform preferinței anterioare)
        self.grades = []
        self.__file_path = file_path
        self.students_service = students_service
        self.subject_service=subject_service
        self.__load_from_file()

    def __ensure_file_exists(self):
        """
        Verifică dacă fișierul există, altfel îl creează.
        """
        try:
            with open(self.__file_path, "a", encoding="utf-8"):
                pass
        except OSError as e:
            print(f"Cannot open grades file: {e}")

    def __load_from_file(self):
        """
        Încarcă datele din fișier în self.grades
        """
        self.__ensure_file_exists()
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split(";")
                    # Format: nota;materie;student
                    if len(parts) >= 3:
                        grade_val = parts[0]
                        subject_name = parts[1]
                        student_name = parts[2]
                        g = Grade(int(grade_val), subject_name, student_name)
                        self.grades.append(g)
                        student = self.students_service.search_student_by_name(student_name)
                        subject = self.subject_service.search_subject_by_name(subject_name)
                        self.students_service.add_grade(student, subject, grade_val)
        except Exception as e:
            print(f"Error loading grades: {e}")

    def __save_to_file(self):
        """
        Salvează lista curentă în fișier.
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for g in self.grades:
                f.write(f"{g.grade};{g.subject};{g.student}\n")

    def add_grade(self, grade):
        """
        Adaugă o notă în memorie și salvează în fișier.
        """
        self.grades.append(grade)
        self.__save_to_file()

    def get_grades(self):
        return self.grades

    # Putem păstra logica de sortare din RepoGrade sau o redefinim aici
    def sort_grades(self):
        return Sorter.insertion_sort(self.grades, key=lambda g: (-g.grade, g.subject, g.student))

    def __len__(self):
        return len(self.grades)