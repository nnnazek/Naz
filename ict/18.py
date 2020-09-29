n = int(input())
a = [int(x) for x in input().split()]
s=a[-1]
print(a[-1])
for i in range(n-1,0,-1):
            a[i] = a[i-1]
a[0]=s
print(a)