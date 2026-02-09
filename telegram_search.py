import platform
import os

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def user():
    global username
    username = input('Введите имя пользователя в формате - username: ')
    return

def info():
    print('[+] username: ', username)
    print('[+] info account: ' + "https://t.me/username_to_id_bot?start="+ username)
    return