duration = int(input('Введите промежуток времени в секундах: '))

minuta = 60
chas = 3600
dn = 86400

if duration <= 60:
    print(duration, 'сек.')

elif 60 < duration < 3600:
    t_minuta = duration // minuta
    t_sek = duration - (t_minuta * 60)
    print(t_minuta, 'мин.', t_sek, 'сек.')

elif 3600 <= duration <= 86400:
    t_chas = duration // chas
    t_minuta = (duration - (t_chas * chas)) // minuta
    t_sek = (duration - (t_chas * chas)) - t_minuta * minuta
    print(t_chas, 'ч.', t_minuta, 'мин.', t_sek, 'сек.')

else:
    t_dn = duration // dn
    t_chas = (duration - (t_dn * dn)) // chas
    t_minuta = ((duration - (t_dn * dn)) - (t_chas * chas)) // minuta
    t_sek = ((duration - (t_dn * dn)) - (t_chas * chas)) - (t_minuta * minuta)
    print(t_dn, 'дн.', t_chas, 'ч.', t_minuta, 'мин.', t_sek, 'сек.')

