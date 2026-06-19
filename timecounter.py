import time

my_time = input("Enter a time in seconds:")
print("Nigga you dont have much time left!")

for x in range (int(my_time), 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"you're remaining time is {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Fuck you NIgga! Times up!!")
