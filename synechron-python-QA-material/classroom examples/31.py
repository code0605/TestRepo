import time
import random
e = ValueError("Too Hot","Engine temperature is very high")


def get_temp():
    return random.randint(50,130)

while True:
    temp = get_temp()
    print(temp)
    if temp > 120:
        raise e
    time.sleep(1)
