import time

my_time = int(input("Enter the amount of time:"))
unit = input("Enter the Unit in (seconds/minutes/hours/days)").lower()

if unit in ["second", "seconds", "s"]:
    total_seconds = my_time
elif unit in ["minute", "minutes", "m"]:
    total_seconds = my_time * 60
elif unit in ["hour", "hours", "h"]:
    total_seconds = my_time * 3600
elif unit in ["day", "days", "d"]:
    total_seconds = my_time * 86400
    
print("Nigga you dont have much time left!")

for x in range ((total_seconds), 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    days = int(x / 86400)
    print(f"you're remaining time is {days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Fuck you NIgga! Times up!!")
