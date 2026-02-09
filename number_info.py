import phonenumbers
from phonenumbers import geocoder, carrier
def get_country_by_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(parsed_number, 'ru')
        return country
    except phonenumbers.NumberParseException:
        return "[+] Неверный номер телефона."
def get_operator_by_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            return "Неверный номер телефона."
        operator = carrier.name_for_number(parsed_number, 'ru')
        return operator if operator else "Оператор не найден."
    except phonenumbers.NumberParseException:
        return "Ошибка при разборе номера телефона."