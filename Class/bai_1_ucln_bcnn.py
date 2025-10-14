# 1.Viết chương trình có sử dụng hàm nhập a,b là số nguyên, dương và kiểm tra điều kiện nhập.
# In ra UCLN và BCNN của 2 số a,b. Yêu cầu viết hàm trả về 2 giá trị ucln và bcnn
import math
def nhap_so():
    print("Nhập 2 số nguyên dương ")
    while True:
        try:
            a = int(input("Nhập Số a = "))
            b = int(input("Nhập Số b = "))
            if a > 0 and b > 0:
                return a, b
            else:
                print()
                print("2 số a và b không phải là số nguyên dương !!!")
        except ValueError:
            print("Vui lòng nhập lại 2 số a và b !!!")


def ucln_bcnn(a,b):
    # ucln
    x,y = a,b
    while y!= 0:
        x,y = y, x%y 
        ucln = x

    # bccn (a*b)//ucln
    bcnn = (a*b)//ucln
    return ucln,bcnn

a,b = nhap_so()
ucln,bcnn = ucln_bcnn(a,b)

print(f"\n UCLN({a},{b}) = {ucln}")
print(f" BCNN({a},{b}) = {bcnn}")

