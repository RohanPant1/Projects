# cook your dish here
t= int(input())

for i in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    a =[]
    c= {}
    d= 1
    for j in range(n):
        if b[j] not in c.keys():
            c[b[j]] = [d, b[j]-1]
            d = d+1
            a.append(c[b[j]][0])
        else:
            a.append(c.get(b[j])[0])
            l = c.get(b[j])
            l[1] = l[1]-1
            c[b[j]] = l
        if c.get(b[j])[1] < 1:
            del c[b[j]]
    if bool(c) == True:
        a.clear()
        a.append(-1)
    print(' '.join(map(str, a))) 