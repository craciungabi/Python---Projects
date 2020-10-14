from datetime import datetime
import random


class Console:
    def __init__(self, car_service, card_client_service, tranzactie_service):
        self.__car_service = car_service
        self.__card_client_service = card_client_service
        self.__tranzactie_service = tranzactie_service

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
            if op == '2':
                self.__show_carduri()
            if op == '3':
                self.__show_tranzactii()
            elif op == 'x':
                break

    def __show_masini(self):
        while True:
            self.__show_menu_masini()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_masini_add()
            elif op == '2':
                self.__ui_remove_masina()

            elif op == '3':
                self.__ui_update_masina()
            elif op == '4':
                self.__show_list((self.__car_service.cautare_masini()))
            elif op == '5':
                self.__show_list(self.__tranzactie_service.ordonare_descr_dupa_manopera())
            elif op == '6':
                self.__car_service.update_garantie()
            elif op == '7':
                self.populateN()
            elif op == 'a':
                self.__show_list(self.__car_service.get_masini())
            elif op == 'b':
                break

    def __show_carduri(self):
        while True:
            self.__show_menu_carduri()
            op = input('Optiune: ')
            if op == '1':
                self.__ui_adauga_card()
            if op == '2':
                self.__ui_remove_card()
            if op == '3':
                self.__ui_update_card()
            if op == '4':
                self.__show_list(self.__card_client_service.cautare_carduri())
            if op == '5':
                print(self.__tranzactie_service.ordonare_descr_dupa_reduceri())
            if op == 'a':
                self.__show_list(self.__card_client_service.get_carduri())
            elif op == 'b':
                break

    def __show_tranzactii(self):
        while True:
            self.__show_menu_tranzactii()
            op = input('Optiune: ')
            if op == '1':
                self.__ui_adauga_tranzactie()
            if op == '2':
                self.__ui_remove_tranzactie()
            if op == '3':
                self.__ui_update_tranzactie()
            if op == '4':
                self.__tranzactie_service.stergere_din_interval()
            if op == '5':
                self.__tranzactie_service.aplicare_reduceri()
            if op == '6':
                self.__show_list(self.__tranzactie_service.tranzactii_in_interval())
            if op == 'a':
                self.__show_list(self.__tranzactie_service.get_tranzactii())
            elif op == 'b':
                break

    def __show_menu_masini(self):
        print('--- Masini ---')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Cautare masini dupa cuvant cheie')
        print('5. Ordonarea masinilor dupa manopera')
        print('6. Update garantie')
        print('7. Populate (n)')
        print('a. Afisare')
        print('b. Back')

    def __show_menu_carduri(self):
        print('--- Carduri ---')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Cautare dupa cuvant cheie')
        print('5. Ordonarea cardurile dupa reduceri')
        print('a. Afisare')
        print('b. Back')

    def __show_menu_tranzactii(self):
        print('--- Tranzactii ---')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Stergere din interval citit')
        print('5. Aplicare reduceri')
        print('6. Afisarea tranzactiilor cu suma intr-un interval dat')
        print('a. Afisare')
        print('b. Back')

    def __handle_masini_add(self):
        """
        Add a car
        :return:
        """
        id_masina = input('Dati ID ul: ')
        while True:
            try:
                id_masina = int(id_masina)
                if self.__car_service.idEx(id_masina) == True:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_masina = input('Dati ID ul:')
            except TypeError:
                print('Trebuie sa introduceti un id inexistent!')
                id_masina = input('Dati ID ul:')

        model = input('Modelul este: ')

        an_achizitie = input('Anul este: ')
        while True:
            try:
                an_achizitie = int(an_achizitie)
                if an_achizitie < 0:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                an_achizitie = input('Dati ID ul:')
            except TypeError:
                print('Anul trebuie sa fie pozitiv')
                an_achizitie = input('Anul este: ')

        nr_km = input('Nr. km sunt: ')
        while True:
            try:
                nr_km = float(nr_km)
                if nr_km < 0:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un float!')
                nr_km = input('Nr. km sunt: ')
            except TypeError:
                print('Kilometrii trebuie sa fie pozitivi')
                nr_km = input('Nr. km sunt: ')

        garantie = input('Garantie(da/nu): ')
        self.__car_service.add_masina(id_masina, model, an_achizitie, nr_km, garantie)

    def __ui_remove_masina(self):
        """
        Removes a car
        :return:
        """
        id_masina = input('Dati ID ul: ')
        while True:
            try:
                id_masina = int(id_masina)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_masina = input('Dati ID ul:')

        self.__car_service.remove_masina(id_masina)
        self.__tranzactie_service.remove_tranzactieCascada(id_masina)

    def __ui_update_masina(self):
        """
        Update a car
        :return:
        """
        id_masina = input('Dati ID ul masinii pe care vreti sa o modificati: ')
        while True:
            try:
                id_masina = int(id_masina)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_masina = input('Dati ID ul:')

        new_model = input('Modelul este: ')

        new_an_achizitie = input('Anul este: ')
        while True:
            try:
                new_an_achizitie = int(new_an_achizitie)
                if new_an_achizitie < 0:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                new_an_achizitie = input('Dati ID ul:')
            except TypeError:
                print('Anul trebuie sa fie pozitiv')
                new_an_achizitie = input('Anul este: ')

        new_nr_km = input('Nr. km sunt: ')
        while True:
            try:
                new_nr_km = float(new_nr_km)
                if new_nr_km < 0:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un float!')
                new_nr_km = input('Nr. km sunt: ')
            except TypeError:
                print('Kilometrii trebuie sa fie pozitivi')
                new_nr_km = input('Nr. km sunt: ')

        new_garantie = input('Garantie(da/nu): ')
        self.__car_service.update_masina(id_masina, new_model, new_an_achizitie, new_nr_km, new_garantie)

    def __show_list(self, objects):
        for obj in objects:
            print(obj)

    def __ui_adauga_card(self):
        """
        Add a card
        :return:
        """
        id_card = input('Dati ID ul: ')
        while True:
            try:
                id_card = int(id_card)
                if self.__card_client_service.idExCard(id_card) == True:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_card = input('Dati ID ul:')
            except TypeError:
                print('Trebuie sa introduceti un card inexistent!')
                id_card = input('Dati ID ul:')

        nume = input('Numele este: ')
        prenume = input('Prenumele este: ')

        cnp = input('Dati CNP ul: ')
        while True:
            try:
                cnp = int(cnp)
                if self.__card_client_service.CnpCard(cnp) == True:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                cnp = input('Dati CNP ul:')
            except TypeError:
                print('Trebuie sa introduceti un cnp care nu exista')
                cnp = input('Dati CNP ul:')

        data_nasterii = input('Data nasterii este (d/m/y): ')
        while True:
            try:
                data_nasterii = datetime.strptime(data_nasterii, '%d/%m/%y').date()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul d/m/yy')
                data_nasterii = input('Data nasterii este (d/m/y): ')
        data_inregistrarii = input('Data inregistrarii este (d/m/y): ')
        while True:
            try:
                data_inregistrarii = datetime.strptime(data_inregistrarii, '%d/%m/%y').date()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul d/m/yy')
                data_inregistrarii = input('Data inregistrarii este (d/m/y): ')

        self.__card_client_service.add_card(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)

    def __ui_remove_card(self):
        """
        Remove a car
        :return:
        """
        id_card = input('Dati ID ul: ')
        while True:
            try:
                id_card = int(id_card)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_card = input('Dati ID ul:')
        self.__card_client_service.remove_card(id_card)

    def __ui_update_card(self):
        """
        Update a card
        :return:
        """
        id_card = input('Dati ID ul pe care vreti sa l modificati: ')
        while True:
            try:
                id_card = int(id_card)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_card = input('Dati ID ul:')

        nume = input('Numele este: ')
        prenume = input('Prenumele este: ')

        cnp = input('Dati CNP ul: ')
        while True:
            try:
                cnp = int(cnp)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                cnp = input('Dati CNP ul:')

        data_nasterii = input('Data nasterii este (d/m/y): ')
        while True:
            try:
                data_nasterii = datetime.strptime(data_nasterii, '%d/%m/%y').date()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul d/m/yy')
                data_nasterii = input('Data nasterii este (d/m/y): ')
        data_inregistrarii = input('Data inregistrarii este (d/m/y): ')
        while True:
            try:
                data_inregistrarii = datetime.strptime(data_inregistrarii, '%d/%m/%y').date()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul d/m/yy')
                data_inregistrarii = input('Data inregistrarii este (d/m/y): ')
        self.__card_client_service.update_card(id_card, nume, prenume, cnp, data_nasterii, data_inregistrarii)

    def __ui_adauga_tranzactie(self):
        """
        Add a transaction
        :return:
        """
        id_tranzactie = input('Dati ID ul tranzactiei: ')
        while True:
            try:
                id_tranzactie = int(id_tranzactie)
                if self.__tranzactie_service.idExTranzactie(id_tranzactie) == True:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_tranzactie = input('Dati ID ul tranzactiei:')
            except TypeError:
                print('Trebuie sa introduceti o tranzactie inexistenta!')
                id_tranzactie = input('Dati ID ul tranzactiei:')

        id_masina = input('Dati ID ul masinii: ')
        while True:
            try:
                id_masina = int(id_masina)
                if self.__car_service.idEx(id_masina) == False:
                    raise TypeError
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_masina = input('Dati ID ul masinii: ')
            except TypeError:
                print('Trebuie sa introduceti o Masina care exista in baza de date!')
                id_masina = input('Dati ID ul masinii: ')

        id_card = input('Dati ID ul cardului: ')
        while True:
            try:
                id_card = int(id_card)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_card = input('Dati ID ul cardului: ')

        if self.__car_service.Garantie(id_masina) == True:
            suma_piese = 0
            print('Deoarece masina este in garantie suma pieselor este 0')
        else:
            suma_piese = input('Dati suma piese: ')
            while True:
                try:
                    suma_piese = float(suma_piese)
                    break
                except ValueError:
                    print('Trebuie sa introduceti un float!')
                    suma_piese = input('Dati suma piese:')

        suma_manopera = input('Dati suma manopera: ')
        while True:
            try:
                suma_manopera = float(suma_manopera)
                break
            except ValueError:
                print('Trebuie sa introduceti un float!')
                suma_manopera = input('Dati suma manopera:')
        data = input('Dati data(d/m/y): ')
        while True:
            try:
                data = datetime.strptime(data, '%d/%m/%y').date()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul d/m/yy')
                data = input('Dati data(d/m/y): ')
        ora = input('Dati ora (h/m): ')
        while True:
            try:
                ora = datetime.strptime(ora, '%H/%M').time()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul (h/m)')
                ora = input('Dati ora (h/m): ')
        if suma_piese == 0:
            print('Deoarece masina este in garantie pentru piese nu platiti nimic')
        else:
            print('Totalul de plata pentru piese este', suma_piese)
        if self.__card_client_service.idExCard(id_card) == True:
            c = suma_manopera
            suma_manopera = 0.9 * suma_manopera
            print('Totalul pentru manopera este', c,
                  'fiind in grantie beneficiati de o reducere de 10%, totalul de plata este', suma_manopera)
        else:
            print('Totalul pentru manopera este: ', suma_manopera)
        self.__tranzactie_service.add_tranzactie(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data,
                                                 ora)

    def __ui_remove_tranzactie(self):
        """
        Remove a transacion
        :return:
        """
        id_tranzactie = input('Dati ID ul tranzactiei: ')
        while True:
            try:
                id_tranzactie = int(id_tranzactie)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_tranzactie = input('Dati ID ul tranzactiei:')
        self.__tranzactie_service.remove_tranzactie(id_tranzactie)

    def __ui_update_tranzactie(self):
        """
        Update a transaction
        :return:
        """
        id_tranzactie = input('Dati ID ul tranzactiei pe care vreti sa o modificati: ')
        while True:
            try:
                id_tranzactie = int(id_tranzactie)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_tranzactie = input('Dati ID ul tranzactiei:')

        id_masina = input('Dati ID ul masinii: ')
        while True:
            try:
                id_masina = int(id_masina)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_masina = input('Dati ID ul masinii: ')

        id_card = input('Dati ID ul cardului: ')
        while True:
            try:
                id_card = int(id_card)
                break
            except ValueError:
                print('Trebuie sa introduceti un int!')
                id_card = input('Dati ID ul cardului: ')

        suma_piese = input('Dati suma piese: ')
        while True:
            try:
                suma_piese = float(suma_piese)
                break
            except ValueError:
                print('Trebuie sa introduceti un float!')
                suma_piese = input('Dati suma piese:')

        suma_manopera = input('Dati suma manopera: ')
        while True:
            try:
                suma_manopera = float(suma_manopera)
                break
            except ValueError:
                print('Trebuie sa introduceti un float!')
                suma_manopera = input('Dati suma manopera:')

        data = input('Dati data(d/m/y): ')
        while True:
            try:
                data = datetime.strptime(data, '%d/%m/%y').date()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul d/m/yy')
                data = input('Dati data(d/m/y): ')
        ora = input('Dati ora (h/m): ')
        while True:
            try:
                ora = datetime.strptime(ora, '%H/%M').time()
                break
            except Exception:
                print('Trebuie sa introduci o data de tipul (h/m)')
                ora = input('Dati ora (h/m): ')
        self.__tranzactie_service.update_tranzactie(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data,
                                                    ora)

    def populateN(self):
        """
        populate n
        :return:
        """
        n = int(input('Adaugati numarul de generari: '))
        for i in range(n):
            self.__car_service.populate()
