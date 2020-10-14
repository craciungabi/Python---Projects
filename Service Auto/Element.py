class Element:

    #current_id = 0

    def __init__(self, id_element):
        self.__id_element = id_element


    @property
    def id_element(self):
        return self.__id_element

    @id_element.setter
    def id_element(self, id_element):
        self.__id_element = id_element
