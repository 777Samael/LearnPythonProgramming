import time
import random

print(time.gmtime(0))

print(time.gmtime(11111143200))

print(time.localtime())

print(time.time())

print("---")

time_here = time.localtime()
print(time_here)
print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)

print("---")

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = time.monotonic()
input("Press enter to stop")

end_time = time.monotonic()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("End at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds.".format(end_time - start_time))
