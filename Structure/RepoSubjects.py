from Exceptions.error_add import ErrorAdd

class RepoSubjects:
    def __init__(self):
        self.__subjects_repo = []

    def __len__(self):
        return len(self.__subjects_repo)

    def add_subject(self, subject):
        """
        This function adds a subject to the subjects list.
        :param subject:
        :return:
        """
        id_subject = subject.get_id_subject()
        subject.set_deleted(False)
        if any(sub.get_id_subject() == id_subject for sub in self.__subjects_repo):
            raise ErrorAdd("There is already a subject with this ID")
        self.__subjects_repo.append(subject)

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