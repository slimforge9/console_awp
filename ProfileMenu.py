from Profile import Profile


class ProfileMenu:
    def __init__(self):

        self.welcome_msg = "Witaj w kreatorze profilu. Profil to wpisanie danych raz, tak abyś nie musiał\n" \
                           "wpisywać tych samych danych za każdym razem gdy uruchamiasz program\n" \
                           "np: twój stopień, imię i nazwisko, jednostka, miejscowość sporządzania protokołu."
        option = input("Wybierz profil: ")
