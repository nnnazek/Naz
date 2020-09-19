x = int(input("first number: "))
y = int(input("second number: "))
z = int(input("third number: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c
print(a, b, c)