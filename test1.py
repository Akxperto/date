
from datetime import datetime
from dateutil import relativedelta
from datetime import date

today = date.today()

# get two dates
d1 = '23/03/2021 12:31:55'
d2 = today.strftime("%d/%m/%Y %H:%M:%S")

# convert string to date object
start_date = datetime.strptime(d1, "%d/%m/%Y %H:%M:%S")
end_date = datetime.strptime(d2, "%d/%m/%Y %H:%M:%S")

# Get the relativedelta between two dates
delta = relativedelta.relativedelta(end_date, start_date)
print('Years, Months, Days between two dates is')
print(delta.years, 'Year(s),', delta.months, 'months,', delta.days, 'days,', delta.hours, 'hours,', delta.minutes, 'minutes, and', delta.seconds, 'seconds')