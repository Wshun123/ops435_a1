#!/usr/bin/env python3
#OPS435 Assignment 1 - Fall 2019
#Program: a1_shunwang.py
#Author: Shun Wang
#The python code in this file (a1_wshun.py) is original work written by Shun Wang. No code in this file is copied from any other source 
#except those provided by the course instructor, including any person, 
#textbook, or on-line resource. I have not shared this python script 
#with anyone or anything except for submission for grading.  
#I understand that the Academic Honesty Policy will be enforced and 
#violators will be reported and appropriate action will be taken.
#!/usr/sbin/env python3


import sys

def usage():
	if ((len(sys.argv) != 4) and len(sys.argv) != 3): 
		print ('Usage: '+ sys.argv[0] + ' [--step] YYYYMMDD +/-n')
		exit()



def dbda(var1,var2):
	i = 0
	total = 0
	result = var1
	if len(str(var2)) == 10:
		valid_date(var2)
		if var1 < var2:
			while result < var2:  
				total +=1
				result = tomorrow(result)
		elif var1 > var2:
			while result > var2:  
				total +=1
				result = yesterday(result)
		print(total) 	

	else:	
		if int(var2) > 0: 
			while i < int(var2):  
				i += 1
				if sys.argv[1] == '--step':
					result = tomorrow(result)
					print(result)
				else:
					result = tomorrow(result)				

				
		elif int(var2) < 0:  
			while i > int(var2):
				i = i - 1
				if sys.argv[1] == '--step':
					result = yesterday(result)
					print(result)
				else:
					result = yesterday(result)			
				
		else:
			result = result

		if sys.argv[1] == '--step':
			print('', end='')
		else:
			print(result)

def leap_year(year_value):
	if (year_value % 4 == 0):
		if (year_value % 100 == 0):
			if (year_value % 400 ==0):
				is_leapyear = True
			else:
				is_leapyear = False
		else:
			is_leapyear = True
	else:
		is_leapyear = False
    		
	return is_leapyear

def days_in_mon(year_value):
	if leap_year(year_value):
		feb = 29
	else:
		feb = 28

	mon_max = { 1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return mon_max

def valid_date(var1):
	if (len(var1) != 10):   
		print("Error: wrong date entered")
		exit()
	else:
		year = int(var1[0:4])
		month = int(var1[5:7])
		day = int(var1[8:])
		mon_max = days_in_mon(year)

		if month not in mon_max.keys():
			print("Error: wrong month entered")
			exit()
		else:
			day_max = mon_max[month]
			if day not in range (1,day_max+1):    
				print("Error: wrong day entered")
				exit()


def tomorrow(var1):
	valid_date(var1)
	year = int(var1[0:4])
	month = int(var1[5:7])
	day = int(var1[8:])
	mon_max = days_in_mon(year)
	tmr_day = day + 1
	
	if tmr_day > mon_max[month]: 
		tmr_day = 1
		month = month + 1
		if month > 12:
			month = 1
			year = year + 1

	next_date = str(year)+'/'+str(month).zfill(2)+'/'+str(tmr_day).zfill(2)
	return next_date
	
def yesterday(var1):
	valid_date(var1)
	year = int(var1[0:4])
	month = int(var1[5:7])
	day = int(var1[8:])
	mon_max = days_in_mon(year)
	yst_day = day - 1
	if yst_day == 0:
		month = month - 1
		if month == 0:
			year = year -1
			month = 12
			yst_day = 31
		else:
			yst_day = mon_max[month]

	day_before = str(year)+'/'+str(month).zfill(2)+'/'+str(yst_day).zfill(2)
	return day_before

if __name__ == "__main__":
	usage()
	if sys.argv[1] == '--step':
		var1 = sys.argv[2]
		var2 = sys.argv[3]
	else:
		var1 = sys.argv[1]
		var2 = sys.argv[2]

	dbda(var1,var2)
