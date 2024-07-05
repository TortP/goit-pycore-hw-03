from datetime import datetime

 # Створюємо функцію
def get_days_from_today(date):
    try:
        # Перетворення рядка дати у об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримання поточної дати
        today_date = datetime.now()
        
        # Розрахунок різниці у днях
        delta = today_date - given_date
        
        # Повернення різниці у днях
        return delta.days
    except ValueError:
        # Обробка випадків неправильного формату дати
        print("Неправильний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.")
        return None

# Приклади використання функції
print(get_days_from_today('2024-07-01'))
