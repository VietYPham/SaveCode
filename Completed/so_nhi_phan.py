#chuyển một số thập phân sang hệ nhị phân 

n = int(input("Nhập Số Thập Phân: "))

bits = []

if n == 0:
    print("Số nhị phân là : 0")
else:
    for i in range(100):
        if n == 0:
            break
        bit = n % 2
        bits.append(str(bit))
        n = n // 2
    
    bits.reverse()

    print("Số Nhị phân là:", "".join(bits))