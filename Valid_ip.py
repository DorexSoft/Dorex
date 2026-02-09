import requests

def is_valid_ip(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            return False
    return True


def get_ip_info(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()

        if 'error' in data:
            print("[+] Ошибка:", data['error']['message'])
        else:
            print(f"[+] IP: {data['ip']}")
            print(f"[+] Местоположение: {data['city']}, {data['region']}, {data['country']}")
            print(f"[+] Организация: {data['org']}")
            print(f"[+] Широта и долгота: {data['loc']}")
    except Exception as e:
        print(f"[+] Произошла ошибка: {e}")