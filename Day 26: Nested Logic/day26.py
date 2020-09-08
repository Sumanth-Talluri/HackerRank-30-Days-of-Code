# Enter your code here. Read input from STDIN. Print output to STDOUT
inp1 = input()
inp2 = input()
d1,m1,y1 = inp1.split()
d2,m2,y2 = inp2.split()
d1 = int(d1)
d2 = int(d2)
m1 = int(m1)
m2 = int(m2)
y1 = int(y1)
y2 = int(y2)
fine = 0

if y1-y2>0:
    fine = 10000
elif m1-m2>0 and y1==y2:
    fine = (m1-m2)*500
elif d1-d2>0 and y1==y2 and m1==m2:
    fine = (d1-d2)*15
else:
    fine = 0

print(fine)
