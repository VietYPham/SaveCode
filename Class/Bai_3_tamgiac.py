# 3. Nhập vào 3 số a,b,c. Kiểm tra 3 số là 3 cạnh tam giác không? 
# Nếu là 3 cạnh tam giác, viết các hàm:
# 3.1 Hiển thị loại của tam giác (đều, vuông-cân, vuông, cân, thường)
# 3.2 Hiển thị độ dài các đường cao
# 3.3 Hiển thị độ dài các đường trung tuyến

import math
def add_canh():
    a = float(input("Nhập cạnh a = "))
    b = float(input("Nhập cạnh b = "))
    c = float(input("Nhập cạnh c = "))
    return a, b, c

def check_tamgiac(a, b, c):
    if a > 0 and b >0 and c >0 and (a+b>c) and (a+c >b) and (b+c >a):
       print()
       print("a,b,c là 3 cạnh của 1 tam giác")
       return True
    else:
        print()
        print("a,b,c không là 3 cạnh của 1 tam giác")
        return False
    
def loai_tamgiac(a,b,c):
    print()
    if a==b==c:
        print(f"tam giác có 3 cạnh (a = {a} ,b = {b} ,c = {c}): là tam giác đều")
    elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
        if a == b and b == c and c==a:
            print(f"tam giác có 3 cạnh (a = {a} ,b = {b} ,c = {c}): là tam giác Vuông cân")
        else: 
            print(f"tam giác có 3 cạnh (a = {a} ,b = {b} ,c = {c}): là tam giác Vuông")
    elif a==b and a==c and b==c:
            print(f"tam giác có 3 cạnh (a = {a} ,b = {b} ,c = {c}): là tam giác cân")
    else:
            print(f"tam giác có 3 cạnh (a = {a} ,b = {b} ,c = {c}): là tam giác Thường")
        
def dt_tamgiac(a,b,c):
    p = (a+b+c)/2
    s= math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

def dodai_dgcao(a,b,c):
     s = dt_tamgiac(a,b,c)
     d1 = (2*s)/a
     d2 = (2*s)/b
     d3 = (2*s)/c
     print()
     print("Độ dài đường cao cạnh a = ",round(d1,2))
     print("Độ dài đường cao cạnh b = ",round(d2,2))
     print("Độ dài đường cao cạnh c = ",round(d3,2))
     return d1,d2,d3
    
def trung_tuyen(a,b,c):
     m1 = 0.5 * math.sqrt(2*b**2 + 2*c**2 - a**2)
     m2 = 0.5 * math.sqrt(2*a**2 + 2*c**2 - b**2)
     m3 = 0.5 * math.sqrt(2*a**2 + 2*b**2 - c**2)
     print()
     print("Độ dài đường trung tuyến cạnh a = ",round(m1,2))
     print("Độ dài đường trung tuyến cạnh b = ",round(m2,2))
     print("Độ dài đường trung tuyến cạnh c = ",round(m3,2))
     return m1,m2,m3


