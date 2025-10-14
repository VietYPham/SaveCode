# Bài 1: Viết một chương trình hiển thị ra màn hình các số từ 1 đến 10

# for i in range (1,11):
#     print(i)

# Bài 2: Viết một chương trình hiển thị ra màn hình các số chẵn từ 1-20

# for i in range (1,21):
#     if i%2 == 0:
#         print(i)


# Bài 3: Viết một chương trình hiển thị ra màn hình các số lẻ từ 1-10

# for i in range (1,11):
#     if i%2 != 0:
#         print(i)

# Bài 4: Viết một chương trình nhập vào từ bàn phím số nguyên dương n. Hiển thị ra màn hình tổng các số chẵn từ 1 đến n

# print("Nhập Số n: ", end="")
# n = int(input(""))
# tong = 0
# if n <= 0:
#     print("Số n không thoả mãn số nguyên dương !!!")
# else:
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             tong += i
#     print("Tổng Số Chẵn: ", end = "")
#     print(tong)

# Bài 5: Viết một chương trình nhập vào từ bàn phím số nguyên dương n. Tính trung bình các các số chẵn từ 1 đến n

# print("Nhập Số n: ", end="")
# n = int(input(""))
# tong = 0
# dem = 0
# if n <= 0:
#     print("Số n không thoả mãn số nguyên dương !!!")
# else:
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             tong += i
#             dem += 1
#     if dem > 0:
#         trung_binh = tong/dem
#         print("Trung Bình Các Số Chẵn = ",round(trung_binh,2))
#     else:
#         print("Không có số chẵn nào thoả mãn trong khoảng từ 1 đến ",n)

# Bài 6: Viết một chương trình nhập vào từ bàn phím số nguyên dương n. Tính và in ra màn hình tổng sau:
# 	   	S1= 1+1/2+1/3+1/4+…+1/n
# 		S2= 2+4+6+8+…+2n
# 		S3 = 1 + 2 + 3 + … + n
# 		S4= 1/3 + 1/5 + … + 1/(2n + 1)

# print("Nhập Số Nguyên n = ",end = "")
# n = int(input(""))
# if n <= 0:
#     print("Số nguyên n không thoả mãn số nguyên dương !!!")
# else:
# ## Cách 1
# tong_1 = 0
# for i in range(1,n+1):
#     tong_1 += 1/i
# print("Tổng S1 = ", round(tong_1,3))

# ## Cách 1
# tong_2 = 0
# tong_2 = n*(n+1)
# print("Tổng S2 = ", round(tong_2,3))

# ## Cách 2
# # tong_2 = 0
# # for i in range (1,n):
# #     tong_2 +=2*(i+1)
# # print("Tổng S2 = ", round(tong_2,3))

# ## Cách 1
# tong_3 = 0
# for i in range(1,n+1):
#     tong_3 +=i
# print("Tổng S3 = ",round(tong_3,3))

# tong_4 = 0
# for i in range (1,n+1):
#     tong_4 += 1/(2*i+1)
# print("Tổng S4 = ",round(tong_4,3))

# Bài 7: Viết một chương trình nhập vào từ bàn phím số nguyên không âm n. Tính và in ra màn hình giá trị của n!

# print("Nhập số nguyên n = ", end="")
# n = int(input(""))

# if n <= 0:
#     print("Số Nguyên n không thoả mãn số nguyên dương !!!")
# else:
#     giai_thua = 1
#     for i in range(1,n+1):
#         giai_thua *= i
#     print("n! = ",giai_thua)

# Bài 8:  Viết một chương trình in ra màn hình các số từ 0-99 như hình sau:
#  	0	1	2	3	4	5	6	7	8	9
# 	10	11	12	13	14	15	16	17	18	19
# 	20	21	22	23	24	25	26	27	28	29
# 	.................
# 	90	91	92	93	94	95	96	97	98	99

# for i in range(0,100):
#     print(i,end = "\t")
#     if (i+1)%10 == 0:
#         print()

# Bài 9: Viết Chương Trình in màn hình *

print("Nhập số dòng ngôi sao mong muốn: n = ", end="")
n = int(input(""))
print()
if n <= 0:
    print("Vui lòng Nhập lại n !!!")
else:
    for i in range(n+1):
        print("* "*(i+1), end=" "*21)
        print("* " * (n-i+1))
