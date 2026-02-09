import requests
import subprocess
import email_search
import number_info
import os
import platform
import number_search
import phone_deanon

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def main():
    clear_console()
    print('''
⠀⠀⢀⣀⣤⣀⠤⣤⣤⣤⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤ 
⠴⣾⣿⣿⣿⣿⢧⣮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧ 
⠀⠘⢿⣿⣿⡏⣾⡿⣣⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⡇ 
⠀⠀⠈⢿⣿⣷⣿⣷⣿⣿⣀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⣿⣿⠿⠟ 
⠀⠀⠀⠈⠛⠋⢿⣷⡻⣿⣿⡷⣴⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿ 
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠁ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣰⣿⣿⣷ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀eye God of death⠀0.2    ⠀⠉⠉⠉⠛⠛⠻⢟⣵⣿⣿
    1. Поиск по номеру
    2. Поиск по почте''')
    function = input('[+] Выберите функцию: ')

    if function == '1' or function == 1:
        number_search.number_serch()
    elif function == '2' or function == 1:
        email_search.check_email()
    else:
        print('Eror')