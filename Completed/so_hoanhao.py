# in ra các số  hoàn hảo nhỏ hơn hoặc bằng n

n = int(input("n= "))
for i in range(2, n+1 ):
    tong_uoc = 0
    for j in range (1,i):
        if i%j == 0:
            tong_uoc += j
    if tong_uoc == i:
        print(i,end = " ")
