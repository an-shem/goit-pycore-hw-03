from datetime import datetime


def get_days_from_today(date: str) -> str:
    if not isinstance(date, str):
        return "Date must be a string."
    date_format = "%Y-%m-%d"
    try:
        date_datetime = datetime.strptime(date, date_format)
        current_datetime = datetime.today()
        difference_days = (current_datetime - date_datetime).days
        return difference_days
    except ValueError:
        return "Incorrect date format"


print(get_days_from_today("2025-09-30"))
print(get_days_from_today("2021-02-24"))
print(get_days_from_today("2027-12-30"))
print(get_days_from_today("2027.12.30"))
print(get_days_from_today("2027/12/30"))
print(get_days_from_today(20250930))
