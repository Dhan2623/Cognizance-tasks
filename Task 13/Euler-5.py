import math
def lcm(n):
    ans = 1
    for i in range(1, n + 1):
        ans = int((ans*i)/math.gcd(ans, i))        
    return ans
t=int(input())
for i in range (t):
    n =int(input())
    print(lcm(n))
    


