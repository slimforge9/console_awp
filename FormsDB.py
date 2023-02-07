class FormsDB:
    # Class that stores needed data of every form

    def __init__(self):
        # Initialization of a dictionary that contains fields in each form
        self.forms_db = {'detain': ['name', 'surname', 'detain_place', 'officer_name', 'officer_unit', 'doc_place',
                                    'detain_time', 'detain_date', 'other_basis', 'doc_time', 'doc_date', 'others',
                                    'family_name', 'dad_name', 'mom_name', 'mom_family', 'p_no', 'birth_place',
                                    'address', 'job', 'ID', 'detain_basis', 'rights', 'health'],
                         'warrant': ['doc_city', 'doc_date', 'doc_time', 'name', 'surname', 'dad_name', 'p_no',
                                     'birth_date', 'birth_place', 'supervisor'],
                         'rej': ['officer_name', 'doc_city', 'doc_date', 'officer_unit', 'officer_id', 'act_time_date',
                                 'act_place', 'act_description', 'offense_base', 'qual', 'item_value',
                                 'how_notify', 'rej_type', 'end_type', 'name', 'surname', 'dad_name',
                                 'mom_name', 'mom_family', 'birth_date', 'birth_place', 'ID', 'address', 'p_no',
                                 'nationality', 'sex', 'job', 'retained_item', 'spb', 'victim', 'subject'],
                         'identity': ['doc_city', 'name', 'surname', 'pic', 'dad_name', 'mom_name', 'mom_family',
                                      'birth_date', 'birth_place', 'p_no', 'address', 'zip_code', 'woj', 'pow', 'gmina',
                                      'nationality', 'officer_unit', 'case', 'officer_name']
                     }


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
