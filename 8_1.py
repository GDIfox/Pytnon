import re


def email_parse(email_address):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)        # структура словаря groupdict с ключами + не учитываем регистры(IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f'wrong email: {email_address}')                                        # ошибочный email
    print(re_email.match(email_address).groupdict())                                             # формирование словаря groupdict


for i in ['someone@geekbrains.ru', 'som&eone@geekbrainsru', 'someone@geekbrainsru']:             #  перебираем все email-ы
    try:
        email_parse(i)
    except ValueError as err:                                                                    # перехватываем снаружи ошибочный email
        print(err)