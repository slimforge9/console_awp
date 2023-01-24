from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colores text in terminal
# colors: black, red, green, yellow, blue, magenta, cyan, and white
colorama_init()


class Translator:
    translator = {
        'detain_place': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Miejsce (adres) zatrzymania osoby:',
        # warrant
        'officer_name': f'{Fore.RED}[Policjant]{Style.RESET_ALL} stopień, imię i nazwisko Policjanta dokonującego czynność'
                        f' {Fore.CYAN}(np: sierż. szt. Adam Nowak): \n{Style.RESET_ALL}',
        'officer_unit': f'{Fore.RED}[Policjant]{Style.RESET_ALL} {Fore.CYAN}- nazwa jednostki policji policjanta {Style.RESET_ALL} (format: KP II Wrzoski):',
        'doc_city': f'{Fore.CYAN}[Dokument]{Style.RESET_ALL} Miejscowość protokołu:',
        'dad_name': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Imię ojca:',
        'birth_place': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Miejsce urodzenia:',
        'supervisor': f'{Fore.CYAN}[Nakaz przyjęcia]{Style.RESET_ALL} stopień, imię i nazwisko, stanowisko kierownika '
                      f'jednostki '
                      f'{Fore.CYAN}(np: mł. insp. Adam Wielicki - Komendant KP I Wilkowyje):\n{Style.RESET_ALL}',
        # detain
        'detain_time': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Godzina zatrzymania {Fore.CYAN}(np: 20:30): {Style.RESET_ALL}',
        'detain_date': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Data zatrzymania osoby {Fore.CYAN}(np: 01.01.1990): {Style.RESET_ALL}',
        'other_basis': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Inna podstawa prawna {Fore.CYAN}(np. art. 79 kkw w zw z art 15 UoP): {Style.RESET_ALL}',
        'others': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Osoby uczestniczące w czynności: ',
        'family_name': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Nazwisko rodowe osoby (nie rodowe matki): ',
        'mom_name': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Imię matki: ',
        'mom_family': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Panieńskie matki: ',
        'job': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Zajęcie: ',
        'ID': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} nazwa, seria i nr dokumentu {Fore.CYAN}(np: DO: AXX 111222){Style.RESET_ALL}: ',
        'detain_basis': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Przyczyna zatrzymania: \n',
        'rights': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Oświadczenie zatrzymanego w zw z poinformowaniem'
                  f' o prawach: \n{Fore.CYAN} (np: swoje prawa zrozumiałem, nie żądam kontaktu z adwokatem i bezpośredniej '
                  f'z nim rozmowy,\n nie żądam powiadomienia osoby najbliższej){Style.RESET_ALL}\n',
        'health': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Oświadczenie zatrzymanego o stanie zdrowia'
                  f' z uwzględnieniem opisu i przyczyn obrażeń:\n {Fore.CYAN}(np: wg oświadczenia zdrowy, nie choruje,'
                  f' nie leczy się psychiatrycznie, odwykowo, neurologicznie)\n{Style.RESET_ALL}',
        'doc_place': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Miejsce sporządzania protokołu: ',
        # rej
        'officer_id': f'{Fore.RED}[Policjant]{Style.RESET_ALL} nr służbowy: ',
        'act_time_date': f'{Fore.CYAN}[Rejestracja KSIP - 119 kw]{Style.RESET_ALL} Data i godzina popełnienia czynu: '
                         f'{Fore.CYAN}(np: 01.01.2023 r., g. 21:37){Style.RESET_ALL}',
        'act_place': f'{Fore.CYAN}[Rejestracja KSIP - 119 kw]{Style.RESET_ALL} Miejsce popełnienia czynu: ',
        'act_description': f'{Fore.CYAN}[Rejestracja KSIP - 119 kw]{Style.RESET_ALL} Opis czynu: ',
        'offense_base': f'{Fore.CYAN}[Rejestracja KSIP - 119 kw]{Style.RESET_ALL} Kwalifikacja prawna'
                        f'{Fore.CYAN} (np: 119 kw){Style.RESET_ALL}',
        'qual': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Kwalifikacjia - szczegóły '
                f'{Fore.CYAN}(np: ze sklepu wielopowierzchniowego){Style.RESET_ALL}',
        'item_value': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Wartość przedmiotu wykroczenia: ',
        'how_notify': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Sposób zawiadomienia: '
                      f'{Fore.CYAN}(np: ustnie){Style.RESET_ALL}',
        'rej_type': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Rodzaj czynności będącej podstawą rejestracji: ',
        'end_type': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Sposób zakończenia czynności przez Policję: '
                    f'{Fore.CYAN}(np: MKK - 500zł){Style.RESET_ALL}',
        'nationality': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Obywatelstwo: ',
        'sex': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Płeć: ',
        'retained_item': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Wskazanie zatrzymanych przedmiotów: ',
        'spb': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Zastosowane środki przymusu: ',
        'victim': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Pokrzywdzona osoba fizyczna: ',
        'subject': f'{Fore.CYAN}[Rejestracja KSIP]{Style.RESET_ALL} Pokrzywdzony podmiot: ',
        'zip_code': f'{Fore.CYAN}[Osoba][Adres]{Style.RESET_ALL} Kod pocztowy: ',
        'woj': f'{Fore.CYAN}[Osoba][Adres]{Style.RESET_ALL} Województwo: ',
        'pow': f'{Fore.CYAN}[Osoba][Adres]{Style.RESET_ALL} Powiat: ',
        'gmina': f'{Fore.CYAN}[Osoba][Adres]{Style.RESET_ALL} Gmina: ',
        'case': f'{Fore.CYAN}[Stw. Tożsamości]{Style.RESET_ALL} do sprawy: '
    }
