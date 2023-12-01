import time

startTime = time.time()
i = 0
while(i < 10000000):
    i = i + 1

print(time.time()-startTime)