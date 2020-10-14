from datetime import datetime
from Domain.Tranzactie import Tranzactie
from Domain.CardClient import CardClient
from Domain.Masina import Masina
from Repository.RepositoryGeneric import Repository

class ServiceTranzactie:

    def __init__(self, repository_tranzactie, repository_card, repository_masina):
        """
        Creates a car service
        :param repository:
        """
        self.__tranzactie_repo = repository_tranzactie
        self.__card_repo = repository_card
        self.__masina_repo = repository_masina

    def add_tranzactie(self, id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora):
        """
        Adauga o noua tranzactie
        :param id_tranzactie:
        :param id_masina:
        :param id_card:
        :param suma_piese:
        :param suma_manopera:
        :param data:
        :param ora:
        :return:
        """

        tranzactie = Tranzactie(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora)
        self.__tranzactie_repo.add_element(tranzactie)

    def update_tranzactie(self, id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora):
        """

        :param id_tranzactie:
        :param id_masina:
        :param id_card:
        :param suma_piese:
        :param suma_manopera:
        :param data:
        :param ora:
        :return:
        """

        tranzactie = Tranzactie(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora)
        self.__tranzactie_repo.update_element(tranzactie)

    def remove_tranzactie(self, id_tranzactie):
        """

        :param id_tranzactie:
        :return:
        """
        list = self.__tranzactie_repo.get_elements()
        for tranazctie in list:
            if tranazctie.get_id_tranzactie() == id_tranzactie:
                self.__tranzactie_repo.remove_element(tranazctie)
                return

    def remove_tranzactieCascada(self, id_masina):
        """

        :param id_tranzactie:
        :return:
        """
        list = self.__tranzactie_repo.get_elements()
        for tranazctie in list:
            if tranazctie.get_id_masina() == id_masina:
                self.__tranzactie_repo.remove_element(tranazctie)
                return

    def stergere_din_interval(self):
        """

        :return:
        """
        start = datetime.strptime(input('Introduceti prima perioada a intervalului (d/m/y): '), '%d/%m/%y').date()
        end = datetime.strptime(input('Introduceti ultima perioada a intervalului (d/m/y): '), '%d/%m/%y').date()
        list = self.__tranzactie_repo.get_elements()
        for tranzactie in list:
            if datetime.strptime(tranzactie.get_data(), '%d/%m/%y').date() > start and datetime.strptime(tranzactie.get_data(), '%d/%m/%y').date() < end:
                self.__tranzactie_repo.remove_element(tranzactie)
                return

    def aplicare_reduceri(self):
        """

        :return:
        """
        lista_tranzactii = self.__tranzactie_repo.get_elements()
        lista_masini = self.__masina_repo.get_elements()
        for tran in lista_tranzactii:
            if tran.get_id_card() != '':
                tran.set_suma_manopera(tran.get_suma_manopera() - 10/100 * tran.get_suma_manopera())
            for car in lista_masini:
                if car.get_id_masina() == tran.get_id_masina():
                    if not car.get_garantie():
                        tran.set_suma_piese(0)

    def tranzactii_in_interval(self):
        """

        :return:
        """
        start = int(input('Dati primul capat al intervalului: '))
        end = int(input('Dati al douilea capat al intervalului: '))
        lista_tranzactii = self.__tranzactie_repo.get_elements()
        lista_finala = []
        for tran in lista_tranzactii:
            suma = tran.get_suma_manopera() + tran.get_suma_piese()
            if start < suma < end:
                lista_finala.append(tran)
        return lista_finala

    def ordonare_descr_dupa_manopera(self):
        """

        :return:
        """
        dict = {}
        list_tranzactii = self.__tranzactie_repo.get_elements()
        lista_masini = self.__masina_repo.get_elements()
        for tran in list_tranzactii:
            for car in lista_masini:
                if car.get_id_masina() == tran.get_id_masina():
                    dict[car.get_id_masina()] = tran.get_suma_manopera()
        return dict

    def ordonare_descr_dupa_reduceri(self):
        """

        :return:
        """
        dict = {}
        lista_tranzactii = self.__tranzactie_repo.get_elements()
        for tran in lista_tranzactii:
            if tran.get_id_card() != '':
                dict[tran.get_id_card()] = 10/100 * tran.get_suma_manopera()

        return dict

    def get_tranzactii(self):
        """
        Returneaza lista cu toate masinile
        :return:
        """
        return self.__tranzactie_repo.get_elements()

    def idExTranzactie(self, id_tranza):
        lista_tranzactii = self.__tranzactie_repo.get_elements()
        for tranz in lista_tranzactii:
            if tranz.get_id_tranzactie() == id_tranza:
                return True
        return False
