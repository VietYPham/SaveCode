# Viết chương trình Python cho phép nhập vào một số nguyên dương,
# sau đó kiểm tra xem số đó có phải là số thuận nghịch hay không.
# (Số thuận nghịch là số đọc xuôi hay ngược đều giống nhau, ví dụ: 121, 12321, 4554.)


# cách 1:

# n = input("Nhập Số nguyên n = ")
# if n == n[::-1]:
#     print(f"n là số thuận nghịch")
# else:
#     print(f"n không là số thuận nghịch")

    # Cách 2:
n = int(input("Nhập Số nguyên n = "))
if n <= 0:
    print("Số n không thoả mãn số nguyên dương, vui lòng nhập lại n !!!")
else: 
    m = n
    dao = 0

    while m > 0:
        dao = dao * 10 + m%10
        m //= 10

    if dao == n:
        print(f"n là số thuận nghịch")
    else:
        print(f"n không là số thuận nghịch")
