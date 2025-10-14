import math
a = float(input("canh 1 = "))
b = float(input("canh 2 = "))
c = float(input("canh 3 = "))
p = (a+b+c)/2
print("Dien tich tam giac = ", math.sqrt(p*(p-a)*(p-b)*(p-c)))
