import re

def check_email():
    email = input('[+] Введите электронную почту: ')
    print('[|]')

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = bool(re.match(email_pattern, email))

    if not is_valid:
        print("""[+] Неверный формат почты.
        """)
        return

    domain = email.split('@')[1]
    local = email.split('@')[0]
    service = None

    if domain == "gmail.com":
        service = "Google/Gmail.com"
    elif domain == "mail.ru":
        service = "Mail.ru"
    elif domain == "yandex.ru":
        service = "Yandex"
    elif domain == "rambler.ru":
        service = "Rambler"
    elif domain == "icloud.com":
        service = "iCloud"
    elif domain == "outlook.com" or domain == "hotmail.com":
        service = "Microsoft Outlook"
    else:
        service = domain

    print(f"""[+] Почта: {email}
[+] Домен: {domain}
[+] Сервис: {service}
[+] Локальная часть: {local}
[+] Valid: True
""")

    print(f"""[+] Dorks:
[|] 
[+] intext:"{local}" @{domain}
[+] "{email}"
[+] site:linkedin.com "{email}"
[+] "{local}" "@{domain}"
""")

    return service, domain, local