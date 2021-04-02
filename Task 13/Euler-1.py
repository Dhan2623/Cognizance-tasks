t=int(input())
for i in range (t):
    n=[]
    test=int(input())
    for i in range(test):
        n.append(i)
    sum = 0
    for i in range(test):
        if n[i]%3 == 0 or n[i]%5 == 0:
            sum = sum + i
    print(sum)

    
