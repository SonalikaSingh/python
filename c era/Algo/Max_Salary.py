#Uses python3

import sys


def fractionalize(i):
    divisor = 9
    while divisor < i:
        divisor = 10 * divisor + 9 

    return i / divisor

def largest_number(a):
    res=""
    for i in range(len(a)):
        a[i]=int(a[i])
    x=(sorted(a, key=fractionalize, reverse=True))
    for i in x:
        res+=str(i)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
    
