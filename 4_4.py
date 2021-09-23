
from datetime import date
from requests import get, utils

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))

def currency_rates(code):
    content = response.split('<Valute ID=')
    d, m, y = map(int, content[0].split('"')[-4].split('.'))

    for i in content:
        if code.upper() in i:
            print(date(year=y, month=m, day=d), end=",")
            print(code.upper(), end=" ")

            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))

if __name__=='__main__':
    print(currency_rates("uSd"))
    print(currency_rates("EUR"))

#######################
import utils

print(utils.currency_rates('@@@'))