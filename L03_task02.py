def info(name, surname, year, city, email, phone):
    print(
        f'{name} {surname}, {year} года рождения, место проживания: {city}, email: {email}, телефон для связи: {phone}')


NAME = input('Введите своё имя: ')
SURNAME = input('Введите свою фамилию: ')
YEAR = input('Введите год своего рожжения: ')
CITY = input('В каком городе / населённом пункте вы живёте? ')
EMAIL = input('Введите email для связи: ')
PHONE = input('Введите телефон для связи: ')
print(info(surname=SURNAME, name=NAME, year=YEAR, city=CITY, email=EMAIL, phone=PHONE))
