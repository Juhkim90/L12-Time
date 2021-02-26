# Time
import time

seconds = time.time()
print (seconds)

countdown = 10

while (countdown >= 0):
	print (countdown)
	countdown -= 1
	time.sleep(1)
else:
	print ("Vrmmmmm!")





'''
# (Optional) Calendar
import calendar

cal = calendar.month(2021, 2)
print (cal)

cal = calendar.TextCalendar(calendar.SUNDAY)
c = cal.formatmonth(2021,2)
print ("Here is the calendar:" )
print (c)
'''