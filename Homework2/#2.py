# Модуль calendar
# Пользователь вводит дату своего рождения в формате DD.MM.YYYY.
# Вывести название дня недели, в который родился пользователь.
# Пользователь вводит название дня недели. Вывести ближайший месяц и год, когда этот день недели выпадал на 1-ое число.


import calendar
import datetime

# Часть 1
a = input('Введите дату в формате DD.MM.YYYY\n')

if len(a) == 10 and a[2] == "." and a[5] == '.':
    year = int(a[6:len(a)])
    month = int(a[3:5])
    day = int(a[0:2])
    d = calendar.weekday(year, month, day)

    # Это работает не так. Должно быть:
    # text_calendar = calendar.TextCalendar()
    # print(text_calendar.formatweekday(d, 9))
    # А можно было вместо использования классов просто использовать calendar.day_name:
    # print(calendar.day_name[d])
    self = calendar.TextCalendar.formatweekday
    print(calendar.TextCalendar.formatweekday(self, d, 9))  # Что здесь значит self, почему без него не работает?
else:
    print('Дата введена в неверном формате ')


# Часть 2
x = input('Введите день недели:\n')
week_days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
dates = []
number_of_days = []

today = datetime.date.today()

# Создаем списки под каждый день недели
# в списке dates - даты когда день недели приходится на 1ое число
# в списке number of days - сколько от сегодня до даты в dates
# Индексы списков всегда будут совпадать по каждой итерации
# Вызываем в списке dates индекс соотв. минимальному количеству дней в списке number of days

if x in week_days:
    for a in range(2018, 2019):
        for b in range(1, 12):
            if calendar.weekday(a, b, 1) == week_days[x]:
                dates.append(datetime.date(a, b, 1))
                number_of_days.append(abs(today - datetime.date(a, b, 1)))
            else:
                continue
    z = dates[number_of_days.index(min(number_of_days))]
    z1 = int(z.month)
    z2 = int(z.year)
    print('Ближайший месяц: %d' % z1)
    print('Ближайший год: %d' % z2)

else:
    print('Неправильно введен день недели, см. варианты ниже:\n')
    print(week_days.keys())

