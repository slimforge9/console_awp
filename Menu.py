from ChoseForms import ChoseForms


class Menu:

    @staticmethod
    def menu():
        option = input("Wybierz opcję: 1. Kreator, 2. O aplikacji 3. Wyjście\n")

        if option == '1':
            cos = ChoseForms()
            chosen_forms = cos.chose_forms()
        return chosen_forms
