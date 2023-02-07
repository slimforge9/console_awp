import json


class Profile:

    def __init__(self, name):
        self.name = name
        self.filename = f'{name.lower()}_data.json'
        self.profile_data = {}

    def collect_data(self):
        self.profile_data['officer_name'] = input("[Policjant] Wpisz swój stopień, imię i nazwisko: ")
        self.profile_data['officer_unit'] = input("[Policjant] jednostka: ")
        self.profile_data['ID'] = input("[Policjant] nr służbowy: ")
        self.profile_data['doc_city'] = input("Miejscowość wykonywanych dokumentów: ")
        self.profile_data['supervisor'] = input("[Stw. Tożsamości] stopień, imię i nazwisko przełożonego w "
                                               "którego dyspozycji zostaje osoba: ")

    def save_profile(self):
        with open(self.filename, "w") as f:
            json.dump(self.profile_data, f)

    def load_profile(self):
        try:
            with open(self.filename, "r") as f:
                self.profile_data = json.load(f)
        except FileNotFoundError:
            self.collect_data()
            self.save_profile()

    def stored_data(self):
        self.load_profile()
        data = self.profile_data
        return data
