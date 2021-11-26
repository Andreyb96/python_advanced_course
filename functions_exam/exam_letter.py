def generate_letter(mail, name, date, time, place, teacher = 'Тимур Гуев', number = 17):
    return 'To: ' + mail + \
    '\nПриветствую, ' + name + \
    '!\nВам назначен экзамен, который пройдет ' + date + ', в ' + time + \
    '.\nПо адресу: ' + place + \
    '.\nЭкзамен будет проводить ' + teacher + ' в кабинете ' + str(number) + '.\nЖелаем удачи на экзамене!'
    