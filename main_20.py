import time
import datetime as d, sys, os, platform
from math import sqrt as s, ceil

time.sleep(3)
print('Hello!')

print(d.datetime.now().time())
print(d.datetime.now().time().hour)
print(sys.path)
print(os.name)
print(platform.system())
print(ceil(s(100)))