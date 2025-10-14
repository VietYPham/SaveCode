import math

# 1. Hàm nhập 3 cạnh


def nhap_canh():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    return a, b, c

# 2. Hàm kiểm tra tam giác


def la_tam_giac(a, b, c):
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

# 3. Hàm tính diện tích tam giác


def dien_tich(a, b, c):
    p = (a + b + c) / 2  # nửa chu vi
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


# --- Chương trình chính ---
a, b, c = nhap_canh()

if la_tam_giac(a, b, c):
    print(f"Ba cạnh {a}, {b}, {c} tạo thành tam giác.")
    print("Diện tích tam giác =", dien_tich(a, b, c))
else:
    print(f"Ba cạnh {a}, {b}, {c} KHÔNG tạo thành tam giác.")
