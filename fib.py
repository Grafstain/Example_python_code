b = 1; c = 2; sum=0
while c <= 4000000:
    sum += c
    for i in range(0, 3):
        a, b = b, c
        c = a+b
        print(c)
print(sum)