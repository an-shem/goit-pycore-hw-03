import re

def normalize_phone(phone_number: str) -> str:
    if not isinstance(phone_number, str):
        return ""
    phone_number = phone_number.strip()
    has_plus = phone_number.startswith("+")
    pattern = r"\D"
    modified_number = re.sub(pattern, "", phone_number)
    if not modified_number or len(modified_number) < 8 or len(modified_number) > 15:
        return ""
    if has_plus or (modified_number.startswith("380") and len(modified_number) == 12):
        return "+" + modified_number
    if modified_number.startswith("0") and len(modified_number) == 10:
        return "+38" + modified_number
    return ""

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
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