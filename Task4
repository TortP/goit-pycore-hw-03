from datetime import datetime, timedelta

# Створюємо функцію
def get_upcoming_birthdays(users):

    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    
    upcoming_birthdays = []

    for user in users:
        # Перетворення дати народження з рядка у об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Оновлення дати народження до поточного року
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року, розглянемо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевірка, чи день народження припадає на наступний тиждень
        if today <= birthday_this_year <= next_week:
            # Переносимо дату привітання на понеділок, якщо день народження припадає на вихідний
            if birthday_this_year.weekday() == 5:  # Субота
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            
            # Додаємо до списку привітань
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "John Doe", "birthday": "1985.07.10"},
    {"name": "Jane Smith", "birthday": "1990.07.12"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
