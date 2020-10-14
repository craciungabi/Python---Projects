from Domain.Masina import Masina


class RepositoryMasina:
    """
    Repository for storing data in memory
    """
    def __init__(self):
        """
        Creates an in memory repository
        """
        self.__storage = []

    def add_masina(self, masina):
        """
        Adauga o noua masina
        :param masina: - masina data
        :return:
        """
        for m in self.__storage:
            if m.get_id_masina() == masina.get_id_masina():
                raise ValueError('ID ul exista deja')
        self.__storage.append(masina)

    def remove_masina(self, masina):
        self.__storage.remove(masina)

    def get_masini(self):
        return self.__storage[:]

    def update_masina(self, masina):
        for i in range(len(self.__storage)):
            if self.__storage[i] == masina.get_id_masina():
                self.__storage[i] = masina
                return

def test_RepositoryMasina():
    r = RepositoryMasina()
    mas = Masina(1, 'model', 12, 54, True)
    r.add_masina(mas)


test_RepositoryMasina()
