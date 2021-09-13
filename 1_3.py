x = 0
while x <= 99:
    x = x + 1
    if (11 <= x <= 14) or 5 <= (x % 10) <= 10 or (x % 10) == 0:
        print(x, 'процентов')
    elif (x % 10) == 1:
        print(x, 'процент')
    elif 1 < (x % 10) <= 4:
        print(x, 'процентa')
