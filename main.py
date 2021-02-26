# Time
import time

seconds = time.time()
print (seconds)

countdown = 5

while (countdown >= 0):
	print (countdown)
	countdown -= 1
	time.sleep(1)
else:
	print ("Vrmmmmm!")

# Multiplication Game
import random

print ("Welcome to the Multiplication Game\n")

# Generates two random numbers in variables.
rand1 = random.randint(1,9)
rand2 = random.randint(1,9)

# Countdown
print ("Here is the Question!")
countdown = 3
while (countdown > 0):
	print (countdown)
	countdown -= 1
	time.sleep(1)
else:
  print ("\n\n")

# Measure Initial Time
ti = time.time()
# Ask user the question
question = int(input(str(rand1) + " x " + str(rand2) + ": "))
# Measure Final Time
tf = time.time()

# Check the answer
# Correct answer, print out correct and elapsed time
if (question == rand1 * rand2):
  print ("Correct")
  print ("Elapsed Time: " + str(tf - ti))
else:
  print ("Nice Try... Wrong answer")






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