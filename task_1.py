from datetime import datetime

def get_days_from_today(date: str) -> str:
    if type(date) is not str:
        return("Date must be a string.")
    date_format = "%Y-%m-%d"
    try:
        date_datetime = datetime.strptime(date, date_format)
        current_datetime = datetime.today()
        difference_days = (current_datetime - date_datetime).days
        return difference_days 
    except ValueError:
        return ("Incorrect date format")