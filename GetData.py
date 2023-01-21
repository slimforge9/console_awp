from FieldInput import FieldInput
from PersonData import PersonData


class GetData:
    # takes person data and fills the fields in every chosen form + asks for data that wasn't input before

    def fill_fields(self):
        # list of fields needed to be filled
        fields_list = FieldInput().give_list()

        # collected person data
        person = PersonData().get_data()

        # chosen forms from Field Input -> menu()
        # chosen_forms = FieldInput.chosen_forms

        # crate dictionary with all needed data
        all_data = dict()
        for data in fields_list:
            print(data)
            all_data[data] = None

        # list of data that we collected
        person_data = list(person.keys())

        # input data which wasn't input
        for field in fields_list:
            if field not in person_data:
                all_data[field] = input(f'Podaj {field}\n')

        # set input into all needed data dictionary
        for k, v in person.items():
            all_data[k] = v

        return all_data



