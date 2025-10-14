import math

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

delta = b**2 + 4*a*c

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương Trình Vô Số Nghiệm")
        else:
            print("Phương Trình Vô Nghiệm")
    else:
        x = -c/b
        print("Phương Trình có 1 nghiệm duy nhất: X = ", round(x,2))
else:
    if delta < 0:
        print("Phương Trình Vô Nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("Phương Trình có Nghiệm kép: X = ", round(x,2))
    else:
        print("Phương Trình có 2 nghiệm phân biệt: ")
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("X1 = ", round(x1,2))
    print("X2= ", round(x2,2))
