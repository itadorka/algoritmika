import datetime

day = int(input('день: '))
month = int(input('месяц: '))
year = int(input('год: '))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    days_in_month[1] = 29

if datetime.date(year, month, day).isoweekday() in [6, 7]:
    next_payday = datetime.date(year, month, day) + datetime.timedelta(days=(9 - datetime.date(year, month, day).isoweekday()))
else:
    next_payday = datetime.date(year, month, 15)
    while next_payday.isoweekday() in [6, 7]:
        next_payday = next_payday + datetime.timedelta(days=1)

days_until_next_payday = (next_payday - datetime.date(year, month, day)).days
print(f"до следующей зарплаты осталось: {days_until_next_payday} дней")
print(f" зарплата {next_payday.strftime('%d-%m-%Y')}, {next_payday.strftime('%A')}")
