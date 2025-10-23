from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    res = []
    today = datetime.today().date()

    for user in users:
        user_birthday_datetime = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = user_birthday_datetime.replace(year=2025)

        if 0 <= ((birthday_this_year - today).days) < 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            if birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            res.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )
    return res


users = [
    {"name": "John Doe", "birthday": "1985.10.30"},
    {"name": "oleh Smith", "birthday": "1990.10.29"},
    {"name": "ivanna Moor", "birthday": "2001.10.26"},
    {"name": "Olga Mayer", "birthday": "1985.10.23"},
    {"name": "Irina Corter", "birthday": "1985.10.25"},
    {"name": "Maya Tiu", "birthday": "1976.11.02"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
