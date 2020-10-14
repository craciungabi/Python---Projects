class Masina:
    """
    Obiect de tip masina
    """
    def __init__(self, id_masina, model, an_achizitie, nr_km, garantie):
        """

        :param id_masina: int
        :param model: string
        :param an_achizitie: int
        :param nr_km: int
        :param garantie: True/False
        """
        self.__id_masina = id_masina
        self.__model = model
        self.__an_achizitie = an_achizitie
        self.__nr_km = nr_km
        self.__garantie = garantie

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id_masina == other.__id_masina

    def get_id_masina(self):
        return self.__id_masina

    def get_model(self):
        return self.__model

    def get_an_achizitie(self):
        return self.__an_achizitie

    def get_nr_km(self):
        return self.__nr_km

    def get_garantie(self):
        return self.__garantie

    def set_id_masina(self, new_id):
        self.__id_masina = new_id

    def set_model(self, new_model):
        self.__model = new_model

    def set_an_achizitie(self, new_an_achizitie):
        self.__an_achizitie = new_an_achizitie

    def set_nr_km(self, new_nr_km):
        self.__nr_km = new_nr_km

    def set_garantie(self, new_garantie):
        self.__garantie = new_garantie

    def get_car_by_id(self, cars, id_car):
        for car in cars:
            if car.get_id_masina() == id_car:
                return car
        return None

    def __str__(self):
        return 'Masina: {}, {}, {}, {}, {}'.format(int(self.__id_masina),
                                                  self.__model,
                                                  int(self.__an_achizitie),
                                                  float(self.__nr_km),
                                                  self.__garantie)






