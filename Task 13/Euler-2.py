t=int(input())
for i in range (t):
   n= int(input())
   n1, n2 = 1,2
   count = 0
   if n<0:
           print("Please enter a positive integer")
   elif n<=1:
           print("the sum of 1 terms is 0")
   else:
        s=2
        n3=0
        while n3< n:
             n3 = n1 + n2
             n1 = n2
             n2 = n3
             if n3%2==0 and n3<n:
                 s=s+n3   
   print(s)      


   
            
    
 

