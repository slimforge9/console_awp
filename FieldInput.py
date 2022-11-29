from Menu import Menu
from FormsDB import FormsDB


class FieldInput:

    # returns chosen forms
    chosen_forms = Menu().menu()

    # needed fields list in chosen forms
    form = FormsDB()
    needed_data = form.get_fields()

    # create list of fields in chosen forms without repetition
    flattened_fields_list = form.fields_list(chosen_forms, needed_data)

    def give_list(self):
        return FieldInput.flattened_fields_list
