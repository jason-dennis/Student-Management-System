from Domain.subject import Subject


class SubjectService:
    def __init__(self, repo_subjects, validator_subject):
        self.repo_subjects = repo_subjects
        self.validator_subject = validator_subject

    def add_subject(self, id, name, professor):
        """
        This function adds a new subject to the repository.
        :param id:
        :param name:
        :param professor:
        :return:
        """
        subject = Subject(id, name, professor)
        self.validator_subject.validate_subjects(subject)
        self.repo_subjects.add_subject(subject)


    def delete_subject(self, id):
        """
        This function deletes a subject from the repository.
        :param id:
        :return:
        """
        subject = self.repo_subjects.search_subject_by_id(id)
        subject.set_deleted(True)

    def modify_subject_name(self, subject, name):
        """
        This function modifies the subject name.
        :param id:
        :param name:
        :return:
        """
        subject.set_name(name)

    def modify_subject_professor(self, subject, professor):
        """
        This function modifies the subject professor.
        :param id:
        :param professor:
        :return:
        """
        subject.set_professor(professor)


    def view_repository_subjects(self):
        """
        This function displays the repository subjects.
        :return:
        """
        return self.repo_subjects.get_all()

    def search_subject_by_id(self,id_student):
        """
        This function searches the student by id.
        :param id_student:
        :return:
        """
        return self.repo_subjects.search_subject_by_id(id_student)

    def search_subject_by_name(self,id_student):
        """
        This function searches the student by id.
        :param id_student:
        :return:
        """
        return self.repo_subjects.search_subject_by_name(id_student)

    