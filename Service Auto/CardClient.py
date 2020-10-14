from datetime import datetime


class CardClient():
    """
    Obiect de tip card-client
    """
    def __init__(self, id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        """

        :param id_card: int
        :param nume: string
        :param prenume: string
        :param cnp: int
        :param data_nasterii: date
        :param data_inregistrarii: date
        """
        self.__id_card = id_card
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        self.__data_nasterii = data_nasterii
        self.__data_inregistrarii = data_inregistrarii

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id_card == other.__id_card

    def get_id_card(self):
        """

        :return:
        """
        return self.__id_card

    def get_nume(self):
        """

        :return:
        """
        return self.__nume

    def get_prenume(self):
        """

        :return:
        """
        return self.__prenume

    def get_cnp(self):
        """

        :return:
        """
        return self.__cnp

    def get_data_nasterii(self):
        """

        :return:
        """
        return self.__data_nasterii

    def get_data_inregistrarii(self):
        return self.__data_inregistrarii

    def set_id_card(self, new_id):
        self.__id_card = new_id

    def set_nume(self, new_name):
        self.__nume = new_name

    def set_prenume(self, new_prenume):
        self.__prenume = new_prenume

    def set_cnp(self, new_cnp):
        self.__cnp = new_cnp

    def set_data_nasterii(self, new_data_nasterii):
        self.__data_nasterii = new_data_nasterii

    def set_data_inregistrarii(self, new_data_inregistrarii):
        self.__data_inregistrarii = new_data_inregistrarii

    def __str__(self):
        return 'Card Client: {}, {}, {}, {}, {}, {}'.format(int(self.__id_card),
                                                      self.__nume,
                                                      self.__prenume,
                                                      int(self.__cnp),
                                                      self.__data_nasterii,
                                                      self.__data_inregistrarii)

