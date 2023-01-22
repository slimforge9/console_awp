from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# colores text in terminal
# colors: black, red, green, yellow, blue, magenta, cyan, and white
colorama_init()


class Translator:
    translator = {
        'detain_place': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Miejsce (adres) zatrzymania osoby:',
        'officer_name': f'{Fore.RED}[Policjant]{Style.RESET_ALL} stopień, imię i nazwisko Policjanta dokonującego czynność'
                        f' {Fore.CYAN}(np: sierż. szt. Adam Nowak): {Style.RESET_ALL}',
        'officer_unit': f'{Fore.RED}[Policjant]{Style.RESET_ALL} {Fore.CYAN}- nazwa jednostki policji policjanta {Style.RESET_ALL} (format: KP II Wrzoski):',
        'doc_city': f'{Fore.CYAN}[Dokument]{Style.RESET_ALL} Miejscowość protokołu:',
        'dad_name': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Imię ojca:',
        'birth_place': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Miejsce urodzenia:',
        'supervisor': f'{Fore.CYAN}[Nakaz przyjęcia]{Style.RESET_ALL} stopień, imię i nazwisko, stanowisko kierownika '
                      f'jednostki '
                      f'{Fore.CYAN}(np: mł. insp. Adam Wielicki - Komendant KP I Wilkowyje):\n{Style.RESET_ALL}',
        'detain_time': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Godzina zatrzymania {Fore.CYAN}(np: 20:30): {Style.RESET_ALL}',
        'detain_date': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Data zatrzymania osoby {Fore.CYAN}(np: 01.01.1990): {Style.RESET_ALL}',
        'other_basis': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Inna podstawa prawna {Fore.CYAN}(np. art. 79 kkw w zw z art 15 UoP): {Style.RESET_ALL}',
        'others': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Osoby uczestniczące w czynności: ',
        'family_name': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Nazwisko rodowe osoby (nie rodowe matki): ',
        'mom_name': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Imię matki: ',
        'mom_family': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Panieńskie matki: ',
        'job': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} Zajęcie: ',
        'ID': f'{Fore.CYAN}[Osoba]{Style.RESET_ALL} nazwa, seria i nr dokumentu {Fore.CYAN}(np: DO: AXX 111222){Style.RESET_ALL}: ',
        'detain_basis': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Przyczyna zatrzymania: ',
        'rights': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Oświadczenie zatrzymanego w zw z poinformowaniem'
                  f' o prawach: \n{Fore.CYAN} (np: swoje prawa zrozumiałem, nie żądam kontaktu z adwokatem i bezpośredniej '
                  f'z nim rozmowy, nie żądam powiadomienia osoby najbliższej){Style.RESET_ALL}\n',
        'health': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Oświadczenie zatrzymanego o stanie zdrowia'
                  f'z uwzględnieniem opisu i przyczyn obrażeń:\n {Fore.CYAN}(np: wg oświadczenia zdrowy, nie choruje,'
                  f'nie leczy się psychiatrycznie, odwykowo, neurologicznie){Style.RESET_ALL}',
        'doc_place': f'{Fore.CYAN}[Protokół Zatrzymania]{Style.RESET_ALL} Miejsce sporządzania protokołu: '

    }
