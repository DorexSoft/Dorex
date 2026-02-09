def Coder1():
    print('''1. leet speak
2. Шифр Цезаря
''')
    code = input('Выберите способ шифрования: ')

    if code == 1 or code == '1':
        substitution_table = {
                'А': 'A', 'Б': '6', 'В': 'B', 'Г': 'r', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': '3', 'И': 'I',
                'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'H', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'C', 'Т': 'T',
                'У': 'Y', 'Ф': 'F', 'Х': 'X', 'Ц': 'Cz', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': "'", 'Ы': 'Y', 'Ь': "'",
                'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'а': 'a', 'б': '6', 'в': 'b', 'г': 'r', 'д': 'd', 'е': 'e', 'ё': 'yo',
                'ж': 'zh', 'з': '3', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'h', 'о': 'o', 'п': 'p',
                'р': 'r', 'с': 'c', 'т': 't', 'у': 'y', 'ф': 'f', 'х': 'x', 'ц': 'cz', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
                'ъ': "'", 'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu', 'я': 'ya'}
        def custom_encrypt(text):
            encrypted = []
            for char in text:
                if char in substitution_table:
                    encrypted.append(substitution_table[char])
                else:
                    encrypted.append(char)
            return ''.join(encrypted)
        text = input("Введите текст для шифрования: ")
        encrypted_text = custom_encrypt(text)
        print("Зашифрованный текст:", encrypted_text)

    elif code == 2 or code == '2':
        substitution_table = {
        'А': 'Г', 'Б': 'Д', 'В': 'Е', 'Г': 'Ё', 'Д': 'Ж', 'Е': 'З', 'Ё': 'И', 'Ж': 'Й', 'З': 'К', 'И': 'Л',
        'Й': 'М', 'К': 'Н', 'Л': 'О', 'М': 'П', 'Н': 'Р', 'О': 'С', 'П': 'Т', 'Р': 'У', 'С': 'Ф', 'Т': 'Х',
        'У': 'Ц', 'Ф': 'Ч', 'Х': 'Ш', 'Ц': 'Щ', 'Ч': 'Ъ', 'Ш': 'Ы', 'Щ': 'Ь', 'Ъ': "Э", 'Ы': 'Ю', 'Ь': "Я",
        'Э': 'А', 'Ю': 'Б', 'Я': 'В', 'а': 'г', 'б': 'д', 'в': 'е', 'г': 'ё', 'д': 'ж', 'е': 'з', 'ё': 'и',
        'ж': 'й', 'з': 'к', 'и': 'л', 'й': 'м', 'к': 'н', 'л': 'о', 'м': 'п', 'н': 'р', 'о': 'с', 'п': 'т',
        'р': 'у', 'с': 'ф', 'т': 'х', 'у': 'ц', 'ф': 'ч', 'х': 'ш', 'ц': 'щ', 'ч': 'ъ', 'ш': 'ы', 'щ': 'ь',
        'ъ': "э", 'ы': 'ю', 'ь': "я", 'э': 'а', 'ю': 'б', 'я': 'в'}
        def custom_encrypt(text):
            encrypted = []
            for char in text:
                if char in substitution_table:
                    encrypted.append(substitution_table[char])
                else:
                    encrypted.append(char)
            return ''.join(encrypted)
        text = input("Введите текст для шифрования: ")
        encrypted_text = custom_encrypt(text)
        print("Зашифрованный текст:", encrypted_text)
    else:
        print('Eror')
        return
