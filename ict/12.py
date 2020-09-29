n = int(input())
i = 1
while n >= 2**i:
    i += 1
    print(2**(i-1))