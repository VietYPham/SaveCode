# # 2. Xây dựng chương trình dạy menu làm các công việc:
# 2.1. Nhập n nguyên >0, kiểm tra điều kiện nhập
# 2.2. Kiểm tra n có nguyên tố không?
# 2.3. Kiểm tra n có là số chính phương?
# 2.4. Kiểm tra n có là số hoàn hảo không?
# 2.5. Kiểm tra n có là số đối xứng không?
# 2.6. Phân tích n thành tích các thừa số nguyên tố
# 2.7. Tìm số nguyên tố nhỏ nhất mà lớn hơn n
# 2.8. Tính tổng các số nguyên tố <=n
# 2.9. Tính tổng các chữ số lẻ của n
# 2.10. Tìm số nguyên tố lớn nhất <=n
import math

# 2.1. Nhập n nguyên >0, kiểm tra điều kiện nhập


def add_n():
    while True:
        try:
            n = int(input("Nhập Số Nguyên n = "))
            if n > 0:
                print()
                print(f"{n} là số nguyên dương thoả mãn")
                return n
            else:
                print()
                print("Số n không phải số nguyên dương !!!")
        except ValueError:
            print("Vui Lòng Nhập lại số n !!!")

# 2.2. Kiểm tra n có nguyên tố không?


def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 2.3. Kiểm tra n có là số chính phương?


def so_chinh_phuong(n):
    m = n
    if int(math.sqrt(m))**2 == m:
        print(f"{n} là số chính phương")
    else:
        print(f"{n} không là số chính phương")

# 2.4. Kiểm tra n có là số hoàn hảo không?


def so_hoan_hao(n):
    if n <= 1:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không là số hoàn hảo")
# 2.5. Kiểm tra n có là số đối xứng không?


def so_doi_xung(n):
    if str(n) == str(n)[::-1]:
        print(f"{n} là số đối xứng")
    else:
        print(f"{n} không là số đối xứng")

# 2.6. Phân tích n thành tích các thừa số nguyên tố
def phan_tich_thua_so(n):
    temp = n
    for i in range (2, n + 1):
        while temp % i == 0:
            print(i, end = " ")
            temp //= i
            if temp > 1:
                print(" * ", end = " ")
        if temp == 1:
            break

# 2.7. Tìm số nguyên tố nhỏ nhất mà lớn hơn n
def so_ntomin(n):
    m = n + 1
    while not so_nguyen_to(m):
        m += 1
    print(f"{m} là số nguyên tố nhỏ nhất mà lớn hơn {n}")
    return m

    
# 2.8. Tính tổng các số nguyên tố <=n
def tong_soNto_min(n):
    tong_st = 0
    for i in range (2, n +1):
        if so_nguyen_to(i):
            tong_st += i
    print(f"Tổng số nguyên tố nhỏ hơn n = {tong_st}")
    return tong_st

# 2.9. Tính tổng các chữ số lẻ của n
def tong_so_le(n):
    tong = 0
    for chr in str(n):
        if int(chr) % 2 == 1:
            tong += int(chr)

    print(f"tổng số lẻ của số n là: {tong}")

# 2.10. Tìm số nguyên tố lớn nhất <=n
def soNto_max(n):
    for i in range(n, 1, -1):
        if so_nguyen_to(i):
            print(f"{i} là số nguyên tố lớn nhất <= {n}")
            return i

#Menu 
while True:
    print()
    print("----- Menu ----- ")
    print("1. Nhập số n từ bàn phím")
    print("2. Kiểm tra n có nguyên tố")
    print("3. Kiểm tra n có là số chính phương")
    print("4. Kiểm tra n có là số hoàn hảo")
    print("5. Kiểm tra n có là số đối xứng ")
    print("6. Phân tích n thành tích các thừa số nguyên tố")
    print("7.  Tìm số nguyên tố nhỏ nhất mà lớn hơn n")
    print("8. Tính tổng các số nguyên tố <=n")
    print("9. Tính tổng các chữ số lẻ của n")
    print("10.  Tìm số nguyên tố lớn nhất <=n")
    print("0. Thoát")   

    print("")
    select = input("Lựa chọn chức năng: ")
    print("")
    if (select == "1"):
        n = add_n()
    elif (select == "2"):
        if so_nguyen_to(n):
            print(f"{n} là số nguyên tố")
        else: 
            print(f"{n} không là số nguyên tố")
    elif (select == "3"):
        so_chinh_phuong(n)
    elif (select == "4"):
        so_hoan_hao(n)
    elif (select == "5"):
       so_doi_xung(n)
    elif (select == '6'):
       phan_tich_thua_so(n)
    elif (select == '7'):
      so_ntomin(n)
    elif (select == '8'):
        tong_soNto_min(n)
    elif (select == '9'):
       tong_so_le(n)
    elif (select == '10'):
        soNto_max(n)
    elif (select == '0'):
        print("")
        print("Thoát Chương Trình !!!")
        break
    else:
        print("Lựa Chọn không hợp lệ, vui lòng nhập lại lựa chọn !!!")