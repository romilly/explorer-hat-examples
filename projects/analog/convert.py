from math import log

def lux(resistance):
   return 300 * (3.0**-log(resistance/3000.0, 2))

for res in [3000, 6000, 10000, 30000, 60000, 100000]:
   # print (300 * 3.0**-log(res/3000, 2))
   print('res %6d = lux %4.1f' % (res, lux(res)))
