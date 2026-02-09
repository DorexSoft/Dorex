import subprocess
import number_info

def number_serch():
    a = input('[+] Введите номер телефона: ')
    code_number = '+' + a
    print(' ')
    print('[+] Страна: ', number_info.get_country_by_phone_number(code_number))
    print('[+] Оператор: ', number_info.get_operator_by_phone_number(code_number))
    print('')
    subprocess.run("python ok_checker.py " + a, shell=True)
    return