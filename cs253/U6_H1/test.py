import datetime
import time
t1 = time.strptime('20120522 15:17:20', "%Y%m%d %H:%M:%S")
a = time.mktime(t1)- time.mktime(time.strptime(datetime.datetime.now().ctime()))

d1 = datetime.datetime(2005, 2, 16)
d2 = datetime.datetime.now()
delta_t = (d1-d2).seconds
print a
print b
