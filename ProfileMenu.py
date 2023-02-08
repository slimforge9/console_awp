import json
import os


from Profile import Profile


class ProfileMenu:
    def __init__(self):

        self.welcome_msg = "Witaj w kreatorze profilu. Profil to wpisanie danych raz, tak abyś nie musiał\n" \
                           "wpisywać tych samych danych za każdym razem gdy uruchamiasz program\n" \
                           "np: twój stopień, imię i nazwisko, jednostka, miejscowość sporządzania protokołu."
        self.filename = 'profiles.json'
        self.profiles = []
        self.prev_profile_name = None
        self.load_profiles()

    def save_profile(self):
        with open(self.filename, "w") as f:
            json.dump(self.profiles, f)

    def load_profiles(self):
        try:
            with open(self.filename, "r") as f:
                self.profiles = json.load(f)
        except FileNotFoundError:
            self.profiles = ['empty', 'pusty', 'brak', '(bez profilu - wpisz ręcznie)']
            self.save_profile()

    def chose_profile(self, nr):
        name = self.profiles[nr-1]
        return Profile(name).stored_data()

    def edit_profile(self, nr):
        self.load_profiles()
        name = self.profiles[nr - 1]
        self.prev_profile_name = self.profiles[nr - 1]
        new_profile_name = Profile(name).edit_data()
        self.profiles[nr - 1] = new_profile_name
        self.save_profile()

    def handle_profile(self, profile):
        choice = input(f"1. Akceptuj profil, 2. Edytuj profil: ")
        if choice == '1':
            return profile
        elif choice == '2':
            self.edit_profile(profile)

    def menu(self):
        while True:
            choice = input(f"Wybierz profil: 1.{self.profiles[0]}, 2.{self.profiles[1]}, 3. {self.profiles[2]},"
                           f"4. {self.profiles[3]}\n")
            if choice == '1':
                return 1
            elif choice == '2':
                return 2
            elif choice == '3':
                return 3
            elif choice == '4':
                return 4
            else:
                print("Nie wybrales profilu")


startMenu = ProfileMenu()
chosen_profile = startMenu.menu()
startMenu.edit_profile(chosen_profile)
# profile_dict = startMenu.chose_profile(chosen_profile)
# ask = Profile(chosen_profile)
# ask.edit_data()
# print(ask.stored_data())


