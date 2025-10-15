#  danh sach

# gan
a = []
b = [1,3,4,2]

# vong lap tinh cac phan thu
c = [i*i for i in range (1,10)]
d = [i*i for i in range (1,10) if i%2==0]

print(*c,d,end = " ") # print(*c) in ra tung phan tu trong list

print("")
e = []
for i in range (1,10):
    if i%2==0:
        e.append(i*i) # cach viet khac cua d
print(e)

# mot so ham hay dung
numbers = [5,4,3,6,2,1]
print(len(numbers)) # dem so phan tu
print(max(numbers)) # tim phan tu lon nhat
print(min(numbers)) # tim phan tu nho nhat
print(sum(numbers)) # tinh tong cac phan tu
numbers.sort() # sap xep tang dan
print(numbers)
(numbers.reverse()) # sap xep giam dan
print(numbers)
