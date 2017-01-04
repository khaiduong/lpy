"""
Write a python script which write to file 64out.txt, each line contains line
index, month, date of month (Feb 28days).

E.g::

  1, January, 31
  2, February, 28
"""
import calendar
from sys import argv 

def write_days_monthname_to_file(year=2016, filename=None):
	try: 
		std_int = int(year)#raw_input(std_int))
	except ValueError:
		print("Please input the year you want to looking for days and months")
		exit(1)
		
	n = 1
	with open('./64out.ext', 'w') as f:
		for i in range(1, 13):
			content = str(n) + ', ' + str(calendar.month_name[i]) +', ' +str(calendar.monthrange(year,i)[1]) + '\n'
			print(content)
			f.write(str(content))
			n +=1

write_days_monthname_to_file(2012)
