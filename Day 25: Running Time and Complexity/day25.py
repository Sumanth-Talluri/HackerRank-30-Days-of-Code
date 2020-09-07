# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
