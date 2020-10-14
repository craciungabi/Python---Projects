import string

from Domain.Masina import Masina
import datetime
from Repository.RepositoryGeneric import Repository
import random

class ServiceMasina:

    def __init__(self, repository):
        """
        Creates a car service
        :param repository:
        """
        self.__repo = repository

    def add_masina(self, id_masina, model, an_achizitie, nr_km, garantie):
        """
        Creeaza o masina
        :param id_masina: int
        :param model: string
        :param an_achizitie: int
        :param nr_km: int
        :param garantie: True/False
        :return:
        """
        if garantie == 'da':
            garantie = True
        else:
            garantie = False
        masina = Masina(id_masina, model, an_achizitie, nr_km, garantie)
        self.__repo.add_element(masina)

    def update_masina(self, id_masina, new_model, new_an_achizitie, new_nr_km, new_garantie):
        """

        :param new_id: int
        :param new_model: string
        :param new_an_achizitie: int
        :param new_nr_km: in
        :param new_garantie: int
        :return:
        """
        if new_garantie == 'da':
            new_garantie = True
        else:
            new_garantie = False
        masina = Masina(id_masina, new_model, new_an_achizitie, new_nr_km, new_garantie)
        self.__repo.update_element(masina)

    def remove_masina(self, id_masina):
        """

        :param id_masina: int
        :return:
        """
        list = self.__repo.get_elements()
        for masina in list:
            if masina.get_id_masina() == id_masina:
                self.__repo.remove_element(masina)
                return

    def cautare_masini(self):
        """
        Cautare full text
        :return: list
        """
        key = input('Introduceti cuvantul cheie dupa care vreti sa fie facuta cautarea: ')
        list = self.__repo.get_elements()
        lista_finala = []
        for car in list:
            if key == car.get_model():
                lista_finala.append(car)
            elif key == str(car.get_an_achizitie()):
                lista_finala.append(car)
            elif key == str(int(car.get_nr_km())):
                lista_finala.append(car)
        return lista_finala

    def update_garantie(self):
        """

        :return:
        """
        lista_masini = self.__repo.get_elements()
        today = datetime.date.today()
        for car in lista_masini:
            if car.get_nr_km() < 60000 and (int(today.strftime("%Y")) - car.get_an_achizitie()) < 3:
                masina = Masina(car.get_id_masina(), car.get_model(), car.get_an_achizitie(), car.get_nr_km(), True)
                self.__repo.update_element(masina)


    def get_masini(self):
        """
        Returneaza lista cu toate masinile
        :return:
        """
        return self.__repo.get_elements()

    def idEx(self, id_mas):
        lista_masini = self.__repo.get_elements()
        for car in lista_masini:
            if car.get_id_masina() == id_mas:
                return True
        return False

    def Garantie(self, id_mas):
        """

        :param id_mas: int
        :return: True/False
        """
        lista_masini = self.__repo.get_elements()
        for car in lista_masini:
            if car.get_id_masina() == id_mas:
                if car.get_garantie() == True:
                    return True
        return False

    def populate(self):
        '''
        Functia populeaza enitatea masini
        :return:
        '''
        letters = string.ascii_lowercase
        id = random.randint(1, 10001)
        model = ''.join(random.choice(letters) for i in range(10))
        yearPurchase = random.randint(1900, 2021)
        noKm = random.randint(0, 200)
        self.add_masina(id, model, yearPurchase, noKm, False)




