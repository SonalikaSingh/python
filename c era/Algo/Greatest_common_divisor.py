# Uses python3
import sys

def gcd(a,b):
    r=0
    if a==0 or b==1:
        return b
    if b==0 or a==1:
        return a
    if a==b:
        return a

    if a>b and a>0 and b>0:
        a,b=b,a%b
        return gcd(a,b)
    if a<b and a>0 and b>0:
        a,b=b%a,a
        return gcd(a,b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    x=gcd(a, b)
    print((a*b)//x)
