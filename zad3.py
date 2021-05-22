def percentage():
    s = input('Введите предложение: ')
    strochnie = 0
    zaglvne = 0
    for i in s:
        if 'a' <= i <= 'z':
            strochnie += 1
        else:
            if 'A' <= i <= 'Z':
                zaglvne += 1
        if 'а' <= i <= 'я':
            strochnie += 1
        else:
            if 'А' <= i <= 'Я':
                zaglvne +=1
    percent1 = strochnie / 100
    percent2 = zaglvne / 100
    res1 = percent1 * 100
    res2 = percent2 * 100
    return strochnie, zaglvne, res1, res2
res = percentage()
print('Первое значение строчные буквы, а второе заглавные, третье и четвертое проценты: ', res)