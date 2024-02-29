import math 
n = int(input())
a = []
l=[]
for p in range(1, n):
    a.append(True)
print(a)
for p in range(2, int((math.sqrt(n)))):
    if a[p]==True:
        j=p*p
        while j<=n:
            a[j]=False
            j=j+p
for p in range(2, n):
    if a[p]==True:
        l[p]=p
print(l)