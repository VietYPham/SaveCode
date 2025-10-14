n = int(input("n = "))

for i in range (1, n+1):
    m = i
    dao = 0

    while m > 0:
        dao = dao*10 + m%10
        m = m // 10

    if dao == i:
        print(i,end = " ")