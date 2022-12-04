class FormsDB:
    # Class that stores needed data of every form

    def __init__(self):
        # Initialization of a dictionary
        self.forms_db = {'detain': ['name', 'surname', 'p_no', 'law_base'],
                         'warrant': ['name', 'surname', 'p_no', 'supervisor']}

    def get_fields(self):
        # returns dictionary of needed data
        return self.forms_db

    def fields_list(self, forms_list, forms_db):
        # takes a list of forms needed to be filled and creates a list without repetition needed fields in those forms
        fields_list = []

        # creates list of lists of stored fields in "forms_list"
        for form in forms_list:
            fields_list.append(forms_db[form])

        # flattens created "fields_list"
        flat_list = [item for sublist in fields_list for item in sublist]

        # creates set of non-duplicated fields
        self.no_repeat = set(flat_list)

        return self.no_repeat



