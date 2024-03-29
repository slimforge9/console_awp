from FieldInput import FieldInput
from PersonData import PersonData
from Translator import Translator

import datetime


class FillFields:
    # takes person data and fills the fields in every chosen form + asks for data that wasn't input before

    # get date and time from system to place in chosen_forms
    time = datetime.datetime.now()
    date = time.strftime("%d.%m.%Y"+' r.')
    hour_minute = time.strftime("%H:%M")

    def fill_fields(self):
        # list of fields needed to be filled
        fields_list = FieldInput().give_list()

        # collected person data
        person = PersonData().get_data()

        # translator for key : terminal_text
        translator = Translator().translator

        # returns text bounded to a key
        def print_text(key):
            return translator[key]

        # crate dictionary with all needed data
        all_data = dict()
        if fields_list:
            for data in fields_list:
                all_data[data] = None
        else:
            pass

        # list of data that we collected
        person_data = list(person.keys())

        # input data which wasn't input
        for field in fields_list:
            if field not in person_data:
                if all_data[field] == 'birth_date':  # ignore birth_date -> it gets it from 'p_no'
                    continue
                elif field == 'doc_date':
                    all_data['doc_date'] = FillFields.date
                elif field == 'doc_time':
                    all_data['doc_time'] = FillFields.hour_minute

                # DODALEM GLIWICE JAKO DOMYSLNE MIASTO
                elif field == 'doc_city':
                    all_data['doc_city'] = f'Gliwice {FillFields.date}'
                elif field == 'pic':
                    continue
                # ~~~~~~~~~~~~~~~~~~~~~~~~
                else:
                    all_data[field] = input(print_text(field)+' ')
                    if field == 'health':
                        if all_data['health'] == '':
                            all_data['health'] = 'wg oświadczenia zdrowy, nie choruje, nie leczy się psychiatrycznie, ' \
                                                 'odwykowo, neurologicznie'
                    if field == 'rights':
                        if all_data['rights'] == '':
                            all_data['rights'] = 'swoje prawa zrozumiałem, nie składam zażalenia do prokuratury na ' \
                                                 'zasadność, legalność i prawidłowość zatrzymania, ' \
                                                 'nie żądam kontaktu z adwokatem i ' \
                                                 'bezpośredniej z nim rozmowy, nie żądam powiadomienia ' \
                                                 'osoby najbliższej'
        print("Czekaj...\n")

        # set input into all needed data dictionary
        for k, v in person.items():
            all_data[k] = v

        return all_data



