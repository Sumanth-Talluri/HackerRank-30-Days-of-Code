# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
while n>0:
    s = input()
    length = len(s)
    s_even = ""
    s_odd = ""
    for i in range(0,length):
        if i%2==0:
            s_even += s[i]
        else:
            s_odd += s[i]
    print(s_even,s_odd)
    n -= 1
