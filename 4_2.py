# requests- http бибилиотека для работы с запросами
import requests

from requests import get, utils
#                   ^запрос, ^красиво вывести объект
response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
#^содержимое "ответа"

def currency_rates(code):
    content = response.split('<Valute ID=')
#                               ^разделитель строки
    for i in content:
        if code.upper() in i:
#                ^перевод всех букв в ерхний регистр (нашего запроса как uSd к USD)
            print(code.upper(), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))
#            retturn Decimal(i.replace("/", "").split("<Value>")[-2].replace(",", "."))
#                     ^исп. в случае когда треб.определенная точность(условия) при  мат.расчетах


print(currency_rates("uSd"))
print(currency_rates("EUR"))
