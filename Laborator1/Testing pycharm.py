import time



N = 10
def countdown (x):
    while x >= 1:
        print (x)
        time.sleep(1)
        x-=1



countdown (N)