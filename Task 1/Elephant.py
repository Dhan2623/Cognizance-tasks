x=int(input("Enter the coordinate of the friend's house(x): "))
if x <= 5:
    print("The minimum number of steps that the elephant needs to make to get from point 0 to point",x,"is 1")
elif x%5 == 0:
    steps=x/5
    print("The minimum number of steps that the elephant needs to make to get from point 0 to point",x,"is",int(steps))
else:
    steps=x/5+1
    print("The minimum number of steps that the elephant needs to make to get from point 0 to point",x,"is",int(steps))
    
