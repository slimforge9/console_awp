class PersonData:

    def __init__(self):
        self.name = input('Imie\n')
        self.surname = input('Nazwisko\n')
        self.p_no = input('PESEL\n')
        self.address = input('Miejsce zamieszkania')
        self.person_data = {'name': self.name,
                            'surname': self.surname,
                            'p_no': self.p_no,
                            'address': self.address
                            }

    def get_data(self):
        return self.person_data
