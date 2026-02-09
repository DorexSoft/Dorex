import requests

def shorten_url(long_url):
    api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.text
    else:
        return "Ошибка при сокращении ссылки"


if __name__ == "__main__":
    long_url = input("Введите длинную ссылку: ")
    short_url = shorten_url(long_url)
    print("Укороченная ссылка:", short_url)