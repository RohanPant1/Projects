import math
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    factors = []
    prime_list=[]
    number = (math.prod(a))
    for j in range(n):
        check = a[j]
        x=0
        while check!=1 or prime_list[x]<=check:
            if check % prime_numbers[x]==0:
                prime_list.append(prime_numbers[x])
                check=check/prime_numbers[x]
                x=0
            else:
                x=x+1
    factor = 1
    size = len(prime_list)
    new_prime_list = []
    for j in range(size):
        for y in range(size):
            for z in range(len(prime_list)):
                factor = factor * prime_list[z]
                factors.append(factor)
            if len(prime_list)>1:
                new_prime_list.append(prime_list[1])
                prime_list.pop(1)

            factor = 1 
        prime_list = new_prime_list
        new_prime_list = []
    factors.append(1)
    print(len(set(factors)))