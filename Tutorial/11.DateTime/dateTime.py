import datetime


today = datetime.datetime.now()

date = datetime.date.today()

# dt = datetime.datetime.strptime(str(today), '%Y-%m-%dT%H:%M:%S%z')

print(repr(today))
print(date)