class Subject:
    def __init__(self, id_subject, name, professor):
        """
        The function create a subject
        :param id_subject: int
        :param name: string
        :param professor: string
        """
        self.__data = {
            "id_subject": id_subject,
            "name": name,
            "professor": professor,
            "deleted": True
        }

    def __str__(self):
        """
        This function returns a string representation of the subject
        :return:
        """
        return f"{self.__data["id_subject"]} | {self.__data["name"]} | {self.__data["professor"]}"
    def get_id_subject(self):
        """
        This function returns the id_subject of the subject
        :return:
        """
        return self.__data["id_subject"]

    def get_name(self):
        """
        This function returns the name of the subject
        :return:
        """
        return self.__data["name"]

    def get_professor(self):
        """
        This function returns the professor of the subject
        :return:
        """
        return self.__data["professor"]

    def is_deleted(self):
        """
        This function returns if this subject is deleted or not
        :return:
        """
        return self.__data["deleted"]

    def set_deleted(self, deleted):
        """
        This function sets this subject to delete
        :param deleted:
        :return:
        """
        self.__data["deleted"] = deleted

    def set_name(self, name):
        """
        This function sets the name of the subject
        :param name:
        :return:
        """
        self.__data["name"] = name

    def set_professor(self, professor):
        """
        This function sets the professor of the subject
        :param professor:
        :return:
        """
        self.__data["professor"] = professor
