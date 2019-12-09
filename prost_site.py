import time
startTimer = time.time()

n=600851475143
if n % 2==0:
    lastFactor=2
    n=n // 2
while n % 2==0:
    n=n // 2
else:
    lastFactor=1
factor=3
maxFactor= n
while n>1 and factor<=maxFactor:
    if n % factor==0:
        n=n // factor
        lastFactor=factor
    while n % factor==0:
        n=n // factor
    maxFactor= n
    factor=factor+2
if n==1:
    print(lastFactor)
else:
    print(n)
endTimer = time.time()
print("It took " + str(endTimer - startTimer) + " seconds!")