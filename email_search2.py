import requests

def check_email(email):
    domain = email.split('@')[1]
    print(f"[+] Домен: {domain}")
    api_url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key=YOUR_API_KEY"
    try:
        response = requests.get(api_url)
        data = response.json()
        if response.status_code == 200 and 'data' in data:
            company_info = data['data']
            print(f"[+] Информация о домене {domain}:")
            print(f"[+] Компания: {company_info.get('organization', 'Неизвестно')}")
            print(f"[+] Сайт: {company_info.get('website', 'Неизвестно')}")
            print(f"[+] Количество найденных адресов: {company_info.get('emails', 'Неизвестно')}")
        else:
            print("[+] Не удалось получить информацию о домене.")
    except Exception as e:
        print(f"[+] Ошибка при запросе информации: {e}")