import time

b = int(time.time())
print(b)
totalMinutes = b//60
print(totalMinutes)
totalDays = totalMinutes//(60*24)
totalYears = totalDays//365
print(totalYears)