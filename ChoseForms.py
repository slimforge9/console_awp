class ChoseForms:
    # Creates list of forms needed to be created,

    def __init__(self):
        self.forms_list = ['detain', 'warrant', '79', 'rej']

    def chose_forms(self):
        # Add or remove form to fill
        chosen_forms = []

        while True:
            option = input("Wybierz opcję: 1 Zatrzymanie, 2. Nakaz, 3. 79, 4. Rej\n"
                           "5. Zakończ")

            if option == '1':
                if self.forms_list[0] not in chosen_forms:
                    chosen_forms.append(self.forms_list[0])
                elif self.forms_list[0] in chosen_forms:
                    chosen_forms.remove(self.forms_list[0])
            elif option == '2':
                if self.forms_list[1] not in chosen_forms:
                    chosen_forms.append(self.forms_list[1])
                elif self.forms_list[1] in chosen_forms:
                    chosen_forms.remove(self.forms_list[1])
            elif option == '3':
                if self.forms_list[2] not in chosen_forms:
                    chosen_forms.append(self.forms_list[2])
                elif self.forms_list[2] in chosen_forms:
                    chosen_forms.remove(self.forms_list[2])
            elif option == '4':
                if self.forms_list[2] not in chosen_forms:
                    chosen_forms.append(self.forms_list[3])
                elif self.forms_list[2] in chosen_forms:
                    chosen_forms.remove(self.forms_list[3])
            else:
                break
            print(chosen_forms)

        return chosen_forms




