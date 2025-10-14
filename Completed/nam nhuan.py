import math

n = int(input("Nhap Nam = "))

if n % 3328 == 0:
    print(f"{n} là nam nhuan kep")
elif (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print(f"{n} la Nam Nhuan")
else:
    print(f"{n} khong la nam nhuan")
