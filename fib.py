num = 1

def F(n):
    if n < 2:
        return n
    else:
        return F(n-2) + F(n-1)

def doFib(num):
    while num < 144:
        num = F(num)
        print(num)

print(F(7))
