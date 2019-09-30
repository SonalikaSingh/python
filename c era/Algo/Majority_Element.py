# Uses python3
import sys

def get_majority_element(a, left, right):
    d=dict.fromkeys(a,0)
    for i in a:
        d[i]+=1

    for i in d:
        if d[i]>(right//2):
            return 1
    return 0
            
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n):
        print(1)
    else:
        print(0)
