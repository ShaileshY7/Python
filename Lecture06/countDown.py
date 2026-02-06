# Print a countdown before something “exciting” happens (like “Launching…” or
# “Happy New Year!”).

import time

count=int(input("Enter countdown to start:"))

for i in range(count,0,-1):
    print(i)
    time.sleep(i)
print("Happy new year")