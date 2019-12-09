import time
startTimer = time.time()

number=33
listNumbers = []  # creates a list to store the factors
f = 2  # defines the first factor
while number > 1:
    if number % f == 0:  # if F is a factor of number
        listNumbers.append(f)  # f is added to the list
        number /= f  # we divide the number by f to proceed
    else:  # if F is not a factor
        f += 1  # we move on to the next number
print(listNumbers[-1])  # returns the list of numbers

endTimer = time.time()
print("It took " + str(endTimer - startTimer) + " seconds!")