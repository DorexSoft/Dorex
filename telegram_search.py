import platform
import os

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def user():
    global username
    username = input('[+] Введите имя пользователя: ')
    return

def info():
    print(f'[+] username: @{username}')
    print('[+] info account: ' + f"https://t.me/username_to_id_bot?start={username}")
    print('')
    return