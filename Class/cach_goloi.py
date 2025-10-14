# điểm rãnh - crack boy

def tinh_tong(a, b):
    tong = a + b
    return tong

def tinh_trung_binh(a, b):
    tong = tinh_tong(a, b)
    tb = tong / 2     # ⚠️ Lỗi: lẽ ra phải chia cho 2
    return tb

x = 10
y = 20
kq = tinh_trung_binh(x, y)
print("Trung bình =", kq)