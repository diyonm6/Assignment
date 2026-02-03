n = int(input("Enter a number: "))
temp = n
s = 0

while temp > 0:
    d = temp % 10
    s += d ** 3
    temp //= 10

if s == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")