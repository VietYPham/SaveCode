# Nhap tháng, xem tháng đó ở quý nào

month = int(input("Nhap Month = "))

if (1 <= month <= 3):
    print("Month", month, "thuộc quý 1")
elif (4 <= month <= 6):
    print("Month", month, "thuộc quý 2")
elif (7 <= month <= 9):
    print("Month", month, "thuộc quý 3")
elif (10 <= month <= 12):
    print("Month", month, "thuộc quý 4")
else:
    print("Tháng", month, "Không Hợp Lệ")
