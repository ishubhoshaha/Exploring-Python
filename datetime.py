# Using Python3

import datetime

print("-----------------------\nCurrent Datetime\n-----------------------")
current_datetime = datetime.datetime.today()
print(current_datetime)
print(current_datetime.day)
print(current_datetime.weekday()) #Monday = 0 while on isoweekday() Monday = 1
current_date = datetime.date.today()
print(current_date)

print("\n-----------------------\nMaking Datetime object\n-----------------------")
current_time = datetime.time(12,33,45,100) # hour,min,sec,microsec
print(current_time)
make_date_time_obj = datetime.datetime(2017,10,22,12,33,45,100) # year,month,day,hour,min,sec,microsec
print(make_date_time_obj)

print("\n-----------------------\nstrftime() -> datetime to string \n-----------------------")
datetimeinstring = current_datetime.strftime('%B %d, %Y - %A')
print (repr(datetimeinstring))
#Syntax- (dateobject).strftime('in what format we want the resultant string')

print("\n-----------------------\nstrptime -> string to datetime \n-----------------------")
print (datetime.datetime.strptime(datetimeinstring,'%B %d, %Y - %A'))
#Syntax- strptime(dateinstring,'in what format the string is right now')

