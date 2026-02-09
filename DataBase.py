import os
import pandas as pd
import platform

def banner():
    print("""
▒█▀▀▄ █▀▀█ ▀▀█▀▀ █▀▀ 
▒█░▒█ █▄▄█ ░░█░░ █▀▀ 
▒█▄▄▀ ▀░░▀ ░░▀░░ ▀▀▀
""")

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def search_in_file(file_path, keyword):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding='utf-8', error_bad_lines=False)
            for index, row in df.iterrows():
                if keyword in row.to_string():
                    print(f"Найдено в {file_path}: {row.to_string()}")

        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df = pd.read_excel(file_path, engine='openpyxl', error_bad_lines=False)
            for index, row in df.iterrows():
                if keyword in row.to_string():
                    print(f"Найдено в {file_path}: {row.to_string()}")

        elif file_path.endswith('.txt') or file_path.endswith('.sql'):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if keyword in line:
                        print(f"Найдено в {file_path}: {line.strip()}")

    except Exception as e:
        print(f"Обработка ошибок {file_path}: {e}")

def search_keyword_in_directory(directory, keyword):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            search_in_file(file_path, keyword)

def main():
    clear_console()
    banner()
    db_directory = 'bases'
    keyword = input("Введите ключевое слово для поиска: ").strip()
    print("Поиск в папке 'bases'...")
    search_keyword_in_directory(db_directory, keyword)
