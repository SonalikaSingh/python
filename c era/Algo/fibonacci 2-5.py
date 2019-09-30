#python3


def fib(n,m):
    if n==0:
        return 0
    if n==1:
        return 1
    
    a=0
    b=1
    r=0
    for i in range(n-1):
        r=(a+b)%m
        a=(b)%m
        b=r
    return r


n,m = map(int, input().split())
print(fib(n, m))
