from Exceptions.error_add import ErrorAdd
from Domain.subject import Subject  # ajustează importul dacă la tine e alt path


class FileRepoSubjects:


    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__subjects_repo = []
        self.__load_from_file()

    def __ensure_file_exists(self):
        """
        This function checks if the file exists
        :return:
        """
        try:
            with open(self.__file_path, "a", encoding="utf-8"):
                pass
        except OSError as e:
            raise ErrorAdd(f"Cannot open subjects file: {e}")

    def __load_from_file(self):
        """
        This function loads the subjects file
        :return:
        """
        self.__ensure_file_exists()
        self.__subjects_repo.clear()

        with open(self.__file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = [p.strip() for p in line.split(";")]
                if len(parts) < 3:
                    continue

                id_subject = int(parts[0])
                name = parts[1]
                professor = parts[2]
                deleted = False
                if len(parts) >= 4:
                    deleted = bool(int(parts[3]))

                sb = Subject(id_subject, name, professor)
                sb.set_deleted(deleted)
                self.__subjects_repo.append(sb)

    def __save_to_file(self):
        """
        This function saves the subjects file
        :return:
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for sb in self.__subjects_repo:
                deleted_flag = 1 if sb.is_deleted() else 0
                f.write(f"{sb.get_id_subject()};{sb.get_name()};{sb.get_professor()};{deleted_flag}\n")

    def __len__(self):
        return len(self.__subjects_repo)

    def add_subject(self, subject):
        """
        This function adds a new subject
        :param subject:
        :return:
        """
        id_subject = subject.get_id_subject()
        subject.set_deleted(False)

        if any(sub.get_id_subject() == id_subject for sub in self.__subjects_repo):
            raise ErrorAdd("There is already a subject with this ID")

        self.__subjects_repo.append(subject)
        self.__save_to_file()

    def search_subject_by_name(self, name):
        """
        This function searches the subject by name.
        :param name:
        :return:
        """
        for subject in self.__subjects_repo:
            if subject.get_name() == name and not subject.is_deleted():
                return subject

        return None

    def search_subject_by_id(self, id):
        """
        This function searches the subject by id.
        :param id:
        :return:
        """
        for subject in self.__subjects_repo:
            if subject.get_id_subject() == id and not subject.is_deleted():
                return subject

        return None

    def get_all(self):
        return self.__subjects_repo