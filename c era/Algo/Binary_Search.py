# Uses python3
import sys

def binary_search(a,left,l, x):
    if left<=l:
        mid=(left+l)//2
        if a[mid]==x:
            return mid;
        if a[mid]>x:
            return binary_search(a,left,mid-1, x)
       
        return binary_search(a,mid+1,l, x)
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    left = 0
    l=len(a)-1
    for x in data[n + 2:]:
        print(binary_search(a,left,l, x), end = ' ')
