
n = int(input("n= "))

for x in range (2,n+1):
    hopso = False
    for y in range(2,round(x**0.5)+1):
        if (x%y==0):
            hopso= True
            break
    if not hopso: print(x,end = " ")  