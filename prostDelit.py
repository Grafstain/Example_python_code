"""
программа находит наибольший простой делитель для числа 600851475143

"""
import time
startTimer = time.time()

lst = [2, ]
n=0
for i in range(3, 7000):
    for j in range(2, i):
        if i % j == 0: #Если i делиться нацело на j то выходим из цикла j
            break
    if i % j != 0:     #Если i не делится на j нацело то добавляем его в конец списка lst
        lst.append(i)
#print(lst)

lst2 = []
for x in lst:          #Для каждого x в списке простых чисел проверяем делится ли на него наше число
    if 600851475143 % x == 0:
        lst2.append(x)
print(lst2[-1])

endTimer = time.time()
print("It took " + str(endTimer - startTimer) + " seconds!")