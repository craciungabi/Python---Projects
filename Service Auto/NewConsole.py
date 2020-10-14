import random
class Console:
    def __init__(self, car_service):
        self.__car_service = car_service

    def __show_menu(self):
        print('1. Masini')
        print('2. Card Client')
        print('3. Tranzactii')
        print('x')

    def run_console(self):
        while True:
            self.__show_menu()
            op = input('Optiune: ')
            if op == '1':
                self.__show_masini()
            elif op == 'x':
                break

    def __show_masini(self):
        while True:
            self.__show_menu_masini()
            op = input('Optiune: ')
            if op == '1':
                self.__populate()
            elif op == 'a':
                self.__show_list(self.__car_service.get_masini())
            elif op == 'x':
                break




    def __show_menu_masini(self):
        print('--- Masini')
        print('1. POPULATE(N)')
        print('a. Afiseaza masini')
        print('x. Iesire')

    def __handle_masini_add(self):
        id_masina = int(input('ID ul: '))
        model = input('Modelul este: ')
        an_achizitie = int(input('Anul este: '))
        nr_km = int(input('Nr. km sunt: '))
        garantie = input('Garantie: ')
        self.__car_service.add_masina(id_masina, model, an_achizitie, nr_km, garantie)

    def __ui_remove_masina(self):
        id_masina = int(input('Dati id ul: '))
        self.__car_service.remove_masina(id_masina)

    def __ui_update_masina(self):
        id_masina = int(input('Dati id ul masinii pe care vreti sa l modificati'))
        new_model = input('Modelul este: ')
        new_an_achizitie = int(input('Anul este: '))
        new_nr_km = int(input('Nr. km sunt: '))
        new_garantie = input('Garantie: ')
        self.__car_service.update_masina(id_masina, new_model, new_an_achizitie, new_nr_km, new_garantie)


    def __p_add_masina(self):

        list_of_strings = ['fds', 'hrrew', 'qwedg', 'gtrwe', 'asd']
        list_of_garanties = ['True', 'False']
        id_masina = random.randint(1, 5)
        model = random.choice(list_of_strings)
        an_achizitie = random.randint(1900, 2019)
        nr_km = random.randint(10, 1000000)
        garantie = random.choice(list_of_garanties)

        while True:
            try:
                self.__car_service.add_masina(id_masina, model, an_achizitie, nr_km, garantie)
                break
            except ValueError:
                id_masina = random.randint(1, 5)
                model = random.choice(list_of_strings)
                an_achizitie = random.randint(1900, 2019)
                nr_km = random.randint(10, 1000000)
                garantie = random.choice(list_of_garanties)



    def __show_list(self, objects):
        for object in objects:
            print(object)

    def __populate(self):
        n = int(input('Adaugati numarul de generari (<=5): '))
        for i in range(n):
            self.__p_add_masina()


