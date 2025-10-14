s1 = "PHAM QUOC VIET"
s2 = s1.lower()     #đổi thành hết chữ thường
print(s2)
print(s2.upper())       # dổi thành hết chữ hoa




cadao_1 = "Trúc xinh, trúc mọc bờ ao"
cadao_2 = "Em xinh, em đứng cùng ai cũng xinh"

print(cadao_1)
print(cadao_2)
print()
cadao_3 = cadao_1.replace("bờ ao","sân đình")
cadao_4 = cadao_2.replace("cùng ai","một mình")
print(cadao_3)
print(cadao_4)

# số lần xuất hiên của "xinh"
print()
print(cadao_1.find("xinh"))

#đếm chữ xuất hiện
print()
print(cadao_2.count("xinh",1,100))

print()
print(len(cadao_1)) # số ký tự của xâu
print(len(cadao_2))
print(len(cadao_3))
print(len(cadao_4))

print()
#kí tự cuối cùng 
print(len(caodao_1)-1)