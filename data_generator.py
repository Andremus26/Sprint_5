import random
import string

def generate_random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_unique_email(domain="@yandex.ru"):
    """Генерирует email вида: test_фамилия_номер_3цифры@domain"""
    surname = "testov"  #  
    cohort = "123"       # номер когорты
    random_digits = ''.join(random.choices(string.digits, k=3))
    name_part = f"test_{surname}_{cohort}_{random_digits}"
    return name_part + domain

def generate_password(length=8):
    return generate_random_string(length)