from datetime import datetime

class Tranzactie():
    def __init__(self, id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora):
        """

        :param id_tranzactie: int
        :param id_masina: int
        :param id_card: int
        :param suma_piese: int
        :param suma_manopera: int
        :param data: date
        :param ora: date
        """
        self.__id_tranzactie = id_tranzactie
        self.__id_masina = id_masina
        self.__id_card = id_card
        self.__suma_piese = suma_piese
        self.__suma_manopera = suma_manopera
        self.__data = data
        self.__ora = ora

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id_tranzactie == other.__id_tranzactie

    def get_id_tranzactie(self):
        return self.__id_tranzactie

    def get_id_masina(self):
        return self.__id_masina

    def get_id_card(self):
        return self.__suma_piese

    def get_suma_piese(self):
        return self.__suma_piese

    def get_suma_manopera(self):
        return self.__suma_manopera

    def get_data(self):
        return self.__data

    def get_ora(self):
        return self.__ora

    def set_id_tranzactie(self, new_tranzactie):
        self.__id_tranzactie = new_tranzactie

    def set_id_masina(self, new_id_masina):
        self.__id_masina = new_id_masina

    def set_id_card(self, new_id_card):
        self.__suma_piese = new_id_card

    def set_suma_piese(self, new_suma_piese):
        self.__suma_piese = new_suma_piese

    def set_suma_manopera(self, new_suma_manopera):
        self.__suma_manopera = new_suma_manopera

    def set_data(self, new_data):
        self.__data = new_data

    def set_ora(self, new_ora):
        self.__ora = new_ora


    def __str__(self):
        return 'Tranzactie: {}, {}, {}, {}, {}, {}, {}'.format(int(self.__id_tranzactie),
                                                               int(self.__id_masina),
                                                               int(self.__id_card),
                                                               float(self.__suma_piese),
                                                               float(self.__suma_manopera),
                                                               self.__data,
                                                               self.__ora)


