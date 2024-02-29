t =int(input())
primes = [0]*1000
for j in range(2, 500):
    if primes[j]==0:
        a = j
        while a<1000:
            primes[a]=primes[a]+1
            a = a+j
for i in range(t):
    n = list(map(int,input().split()))
    k = n[2]
    final = 0
    for j in range(n[0], n[1]+1):
        if primes[j]==k:
            final = final + 1
    print(final)