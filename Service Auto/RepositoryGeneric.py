import pickle


class Repository:
    """
    Repository for storing data in memory
    """

    def __init__(self, file_name):
        """
        Creates an in memory repository
        """
        self.__storage = []
        self.__file_name = file_name

    def __load_from_file(self):
        try:
            with open(self.__file_name, "rb") as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()

    def __save_to_file(self):
        with open(self.__file_name, "wb") as f_write:
            pickle.dump(self.__storage, f_write)

    def add_element(self, element):
        """
        Adauga o noua masina
        :param element: - masina data
        :return:
        """
        self.__load_from_file()
        self.__storage.append(element)
        self.__save_to_file()

    def read(self, id_element=None):
        """

        :param id_element:
        :return:
        """
        self.__load_from_file()
        if id_element is None:
            return self.__storage
        if id_element in self.__storage:
            for obj in self.__storage:
                if obj.id_element == id_element:
                    return obj
        return None

    def remove_element(self, element):
        self.__load_from_file()

        if element not in self.__storage:
            raise ValueError('ID inexistent')

        for i in range(len(self.__storage)):
            if self.__storage[i] == element:
                del self.__storage[i]
                self.__save_to_file()
                return

    def get_elements(self):
        self.__load_from_file()
        return self.__storage[:]

    def update_element(self, element):
        self.__load_from_file()

        if element not in self.__storage:
            raise ValueError('ID inexistent')
        for i in range(len(self.__storage)):
            if element == self.__storage[i]:
                self.__storage[i] = element
        self.__save_to_file()

import pickle

class GenericFileRepository:
    def __init__(self, filename):
        self.__filename = filename

    def __read_file(self):
        try:
            with open(self.__filename, 'rb') as f:
                return pickle.load(f)
        except:
            return []

    def __save_file(self, to_save):
        with open(self.__filename, 'wb') as f:
            pickle.dump(to_save, f)

    def read(self, id_entity=None):
        if id_entity is None:
            return self.__read_file()
        for entity in self.__read_file():
            if entity.id_entity == id_entity:
                return entity
        return None

    def add(self, entity):

        entities = self.__read_file()
        if self.read(entity.id_entity) is not None:
            raise KeyError('ID exists!')
        entities.append(entity)
        self.__save_file(entities)

    def remove(self, id_entity):
        entities = self.__read_file()

        for i in range(len(entities)):
            if entities[i].id_entity == id_entity:
                del entities[i]
                self.__save_file(entities)
                return

    def update(self, entity):
        entities = self.__read_file()
        for i in range(len(entities)):
            if entity == entities[i]:
                entities[i] = entity
        self.__save_file(entities)