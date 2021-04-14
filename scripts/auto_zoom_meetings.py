from datetime import datetime
import calendar
import os
import csv
from time import sleep
from pync import Notifier

import os

# The notifier function
def notify(title, link, message):
	t = '-title {!r}'.format(title)
	m = '-message {!r}'.format(message)
	o = '-open {!r}'.format(link)
	s= '-sound Crystal'
	os.system('terminal-notifier {}'.format(' '.join([t, m, o, s])))
# Calling the function

notify(title = 'Auto Zoom', link = 'http://google.com', message  = 'Background')

while True:

	now = datetime.now()
	day_index = datetime.today().weekday()
	day = calendar.day_name[day_index]
	hour = now.hour
	minute = now.minute
	try:
		with open('calendar.csv', newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print()
				print(day, hour, minute)
				print(row['day'], row['hour'], row['minute'], row['title'], row['link'])
				print()
				if str(row['day']) == str(day) and str(row['hour']) == str(hour) and str(row['minute']) == str(minute):
					notify(title='Zoom Call', message=row['title'], link=row['link'])
					#os.system("open -a 'Google Chrome' " + row['link'])
					#Notifier.notify(row['title'], open=row['link'])
				break

			sleep(10)
	except:
		None

			