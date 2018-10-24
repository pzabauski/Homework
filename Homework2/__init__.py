import calendar
import datetime

x = input('Введите день недели:\n')
week_days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
the_closest_date_to_today = {}
dates = []
number_of_days = []

today = datetime.date.today()

if x in week_days:
    for a in range(2018, 2019):
        for b in range(1, 12):
            if calendar.weekday(a, b, 1) == week_days[x]:                      # Создаем списки по каждый день недели
                dates.append(datetime.date(a, b, 1))                           # в списке dates - даты когда день недели приходится на 1ое число
                number_of_days.append(abs(today - datetime.date(a, b, 1)))     # в списке number of days - сколько от сегодня до даты в списке выше
            else:
                continue
    print(dates[number_of_days.index(min(number_of_days))])                     # Вызываем в списке dates индекс соотв. минимальному количеству дней в списке number of days
else:
    print('Неправильно введен день недели, см. варианты ниже:\n')
    print(week_days.keys())


