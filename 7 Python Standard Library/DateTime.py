from datetime import date

#today = date(2025, 1, 2)

worldcup_2026 = date(2026, 11, 22)
print(worldcup_2026)

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

some_day = date.fromordinal(780300)
print(some_day)


ld = "2022-11-09"
another_day = date.fromisoformat(ld)
print(another_day)


day_to_worldcup = worldcup_2026 - today
print(day_to_worldcup)

print(type(day_to_worldcup))

print(today > worldcup_2026)

print(worldcup_2026.isoformat())

from datetime import time

time1 = time()

time2 = time(hour=14, minute=29,second=59 )

print(time2)

time3 = time.fromisoformat('11:44:50')

print(time3)

from datetime import datetime

MyProject_date = datetime(year=2022, month=11, day=7,hour=11, minute=30, second=1)
print(MyProject_date)

now = []
now.append(datetime.now())
print(now)

itstoday = datetime.today()
print(itstoday)

worldcup_2022 = datetime.fromisoformat('2022-11-21 13:00:00')
print(worldcup_2022)

countdown = now[0] - worldcup_2022
print("Count down: ", countdown)


from datetime import timedelta

delta = timedelta(days=20 , seconds=29, minutes=55, hours=4, weeks=3)

now2 = datetime.now()

print(now2 - delta)


print(now2.strftime("%A, %d/%B/%Y"))
