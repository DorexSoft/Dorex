import requests
import subprocess

def check_email():
    email = input('[+] Введите электронную почту: ')
    print('')
    domain = email.split('@')[1]
    print(f"[+] Домен: {domain}")
    subprocess.run("python ok_checker.py " + email, shell=True)