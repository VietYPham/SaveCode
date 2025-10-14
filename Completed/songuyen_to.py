# in số nguyên tố

a = int(input("Nhập số đầu: "))
b = int(input("Nhập số cuối: "))

print("Các số nguyên tố trong khoảng từ", a, "đến", b, "là: ")

for n in range(a, b+1):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
                
            print(n, end=" ")
