'''
using python3
- pip install pytz
- importance of timezone: https://julien.danjou.info/blog/2015/python-and-timezones
- all available pytz timezone : https://gist.github.com/pamelafox/986163
'''
import datetime
import pytz

print("-----------------------\nDifference Between today(), now(), utcnow()\n-----------------------")
dattime_today = datetime.datetime.today() # give local current time
dattime_now = datetime.datetime.now(tz = pytz.UTC) # now accept timezone parameter but other two don't
dattime_utcnow = datetime.datetime.utcnow() # give current utc time but we couldn't able to change the timezone
print (dattime_today)
print (dattime_now)
print (dattime_utcnow)

print("-----------------------\nUse different timezone\n-----------------------")
print (dattime_now.astimezone(pytz.timezone('Asia/Calcutta')))

print("-----------------------\nConvert 'navive/local/timezone unware time' to equivalent specific timezone time\n-----------------------")
naive_time = datetime.datetime.today()
my_current_timezone = pytz.timezone('Asia/Dhaka')
localize_naive_time = my_current_timezone.localize(naive_time)
equivalent_calcutta_time = localize_naive_time.astimezone(pytz.timezone('Asia/Calcutta'))
print (equivalent_calcutta_time)

print("-----------------------\nGet all available timezone\n-----------------------")
# for t in pytz.all_timezones:
# 	print (t)
