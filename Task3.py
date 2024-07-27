import re

#Створюємо фунцію
def normalize_phone(phone_number):
    # Видалення всіх символів, крім цифр та '+'
    normalized_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
    # Перевірка, чи номер починається з '+'
    if not normalized_number.startswith('+'):
        if normalized_number.startswith('380'):
            # Якщо номер починається з '380', додаємо лише '+'
            normalized_number = '+' + normalized_number
        else:
            # Інакше додаємо '+38' на початок номера
            normalized_number = '+38' + normalized_number
    
    return normalized_number

# Приклади використання функції
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
