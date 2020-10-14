from Domain.CardClient import CardClient
from Repository.RepositoryGeneric import Repository

class ServiceCard:

    def __init__(self, repository):
        """
        Creates a car service
        :param repository:
        """
        self.__repo = repository

    def add_card(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        """

        :param id_card: int
        :param nume: string
        :param prenume: string
        :param cnp: int
        :param data_nasterii: date
        :param data_inregistrarii: date
        :return:
        """
        card = CardClient(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)
        self.__repo.add_element(card)

    def update_card(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        """

        :param id_card: int
        :param nume: string
        :param prenume: string
        :param cnp: int
        :param data_nasterii: date
        :param data_inregistrarii: date
        :return:
        """
        card = CardClient(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)
        self.__repo.update_element(card)

    def remove_card(self, id_card):
        """

        :param id_card: int
        :return:
        """
        list = self.__repo.get_elements()
        for card in list:
            if card.get_id_card() == id_card:
                self.__repo.remove_element(card)
                return

    def get_carduri(self):
        """
        Returneaza lista cu toate masinile
        :return:
        """
        return self.__repo.get_elements()

    def cautare_carduri(self):
        """
        Cautare full text
        :return: list
        """
        key = input('Introduceti cuvantul cheie dupa care vreti sa fie facuta cautarea')
        list = self.__repo.get_elements()
        lista_finala = []
        for card in list:
            if key == str(card.get_nume()):
                lista_finala.append(card)

            elif key == str(card.get_prenume()):
                lista_finala.append(card)

            elif key == str(card.get_cnp()):
                lista_finala.append(card)

            elif key == str(card.get_data_nasterii()):
                lista_finala.append(card)

            elif key == str(card.get_data_inregistrarii()):
                lista_finala.append(card)
        return lista_finala

    def idExCard(self, id_card):
        """

        :param id_card: int
        :return: True/False
        """
        lista_carduri = self.__repo.get_elements()
        for cards in lista_carduri:
            if cards.get_id_card() == id_card:
                return True
        return False

    def CnpCard(self, CNP):
        lista_carduri = self.__repo.get_elements()
        for c in lista_carduri:
            if c.get_cnp() == CNP:
                return True
        return False