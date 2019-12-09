
import time
startTimer = time.time()


sum = 0; b = 1; c = 2
while c < 4000000:
    sum = sum + c
    for i in range(0,3):    #count each 3,
        a, b = b, c
        c = a + b

print(sum)
endTimer = time.time()
print("It took " + str(endTimer - startTimer) + " seconds!")