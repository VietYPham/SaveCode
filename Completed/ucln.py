a = int(input("a = "))
b = int(input("b = "))

# Trường hợp đặc biệt
if a == 0 and b == 0:
    gcd = 0   # gcd(0,0) thường quy ước = 0
elif a == 0:
    gcd = b
elif b == 0:
    gcd = a
else:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
gcd = a
print(f"gcd({a},{b}) = {gcd}")